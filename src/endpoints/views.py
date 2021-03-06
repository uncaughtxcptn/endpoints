from aiohttp_jinja2 import template
from aiohttp import web

from db import Endpoint, AccessLog, Response

from datetime import datetime

import json

from redis_channel import get_sub_channel

from sqlalchemy import desc

from utils import get_http_request_string, get_response_data

import uuid


@template('index.html')
async def index(request):
    pass


async def visit_endpoint(request):
    hash_value = request.match_info['hash']
    db = request.app['db']
    redis = request.app['pub_channel']
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
        channel = await redis.pubsub_channels(hash_value)
        try:
            channel = channel[0]
        except IndexError:
            pass
        else:
            channel_msg = {
                'type': 'access-log',
                'data': {
                    'id': access_log.id,
                    'request': access_data['request'],
                    'response': access_data['response'],
                    'when': datetime.utcnow().isoformat()
                }
            }
            redis.publish(channel, json.dumps(channel_msg))
        return response_obj


async def sockets(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    hash_value = request.match_info['hash']
    channel, redis = await get_sub_channel(request.app, hash_value)
    try:
        while await channel.wait_message():
            data = await channel.get(encoding='utf-8')
            ws.send_str(data)
    except Exception:
        pass
    redis.close()
    return ws


async def create_endpoint(request):
    db = request.app['db']
    async with db.acquire() as conn:
        async with conn.begin():
            hash_value = uuid.uuid4().hex
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


async def get_auto_response(request):
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
        result = await conn.execute(
            response_t.select().where(response_t.c.endpoint_id == endpoint.id)
            .order_by(desc(response_t.c.id)))
        response = await result.first()
        if response is None:
            response_data = {
                'headers': [{'name': '', 'value': ''}],
                'responseBody': '',
                'statusCode': 200}
        else:
            _headers = json.loads(response.headers)
            headers = []
            for k, v in _headers.items():
                headers.append({'name': k, 'value': v})
            response_data = {
                'headers': headers,
                'responseBody': response.body,
                'statusCode': response.status_code}
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
