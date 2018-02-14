from aiohttp_jinja2 import template
from aiohttp import web, WSMsgType

from db import Endpoint, AccessLog, Response

from datetime import datetime

import json

from sqlalchemy import desc

from utils import get_http_request_string, get_response_data

import uuid


@template('index.html')
async def index(request):
    pass


async def visit_endpoint(request):
    hash_value = request.match_info['hash']
    db = request.app['db']
    endpoint_t = Endpoint.__table__
    accesslog_t = AccessLog.__table__
    async with db.acquire() as conn:
        result = await conn.execute(
            endpoint_t.select().where(endpoint_t.c.hash == hash_value).where(
                endpoint_t.c.live == True))
        endpoint = await result.first()
        if endpoint is None:
            raise web.HTTPNotFound()
        response_obj, response_string = await get_response_data(
            endpoint=endpoint, conn=conn)
        access_data = {
            'endpoint_id': endpoint.id,
            'request': await get_http_request_string(request),
            'response': response_string,
        }
        access_log = await conn.execute(
            accesslog_t.insert().values(access_data))
        access_log = await access_log.fetchone()
        ws = request.app['sockets'].get(hash_value)
        if ws:
            ws.send_str(json.dumps(
                {'type': 'access-log',
                 'data': {
                        'id': access_log.id,
                        'request': access_data['request'],
                        'response': access_data['response'],
                        'when': datetime.utcnow().isoformat()
                        }
                 }))
        return response_obj


async def create_endpoint(request):
    db = request.app['db']
    async with db.acquire() as conn:
        async with conn.begin():
            hash_value = str(uuid.uuid4().hex)
            data = await conn.execute(
                Endpoint.__table__.insert().values({'hash': hash_value}))
            data = await data.fetchone()
    return web.json_response({'id': data.id, 'hash': hash_value})


async def view_access_logs(request):
    hash_value = request.match_info['hash']
    db = request.app['db']
    endpoint_t = Endpoint.__table__
    accesslog_t = AccessLog.__table__
    async with db.acquire() as conn:
        result = await conn.execute(
            endpoint_t.select().where(endpoint_t.c.hash == hash_value))
        endpoint = await result.first()
        if endpoint is None:
            raise web.HTTPNotFound()
        result = await conn.execute(
            accesslog_t.select().where(
                accesslog_t.c.endpoint_id == endpoint.id).
            order_by(desc(accesslog_t.c.id)))
        access_logs = await result.fetchall()
        logs = []
        for access_log in access_logs:
            logs.append(
                {'id': access_log.id,
                 'request': access_log.request,
                 'response': access_log.response,
                 'when': access_log.when.isoformat()})
        return web.json_response(logs)


async def set_response_data(request):
    hash_value = request.match_info['hash']
    db = request.app['db']
    endpoint_t = Endpoint.__table__
    response_t = Response.__table__
    async with db.acquire() as conn:
        result = await conn.execute(
            endpoint_t.select().where(endpoint_t.c.hash == hash_value))
        endpoint = await result.first()
        if endpoint is None:
            raise web.HTTPNotFound()
        post_data = await request.post()
        status_code = post_data.get('statusCode', 200)
        try:
            headers = json.loads(post_data.get('headers'))
        except TypeError:
            headers = []
        response_body = post_data.get('responseBody', '')
        header_dict = {}
        for item in headers:
            header_dict[item['name']] = item['value']
        headers = json.dumps(header_dict)
        response_data = {
            'headers': headers,
            'body': response_body,
            'status_code': status_code,
            'endpoint_id': endpoint.id}
        await conn.execute(response_t.insert().values(response_data))
    return web.json_response(response_data)


class EndpointLiveView(web.View):

    async def get_endpoint(self, conn):
        endpoint_t = Endpoint.__table__
        hash_value = self.request.match_info['hash']
        endpoint = await conn.execute(
            endpoint_t.select().where(endpoint_t.c.hash == hash_value))
        endpoint = await endpoint.first()
        if endpoint is None:
            raise web.HTTPNotFound()
        return endpoint

    async def get(self):
        db = self.request.app['db']
        async with db.acquire() as conn:
            endpoint = await self.get_endpoint(conn)
            return web.json_response({'live': endpoint.live})

    async def post(self):
        db = self.request.app['db']
        hash_value = self.request.match_info['hash']
        endpoint_t = Endpoint.__table__
        async with db.acquire() as conn:
            post_data = await self.request.post()
            live = int(post_data.get('live', 1)) == 1
            values = {'live': live}
            await conn.execute(
                endpoint_t.update().where(endpoint_t.c.hash == hash_value).
                values(values))
            return web.json_response(values)


async def sockets(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    hash_value = request.match_info['hash']
    request.app['sockets'][hash_value] = ws
    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
    del request.app['sockets'][hash_value]
    print('closing ws connection')
    return ws
