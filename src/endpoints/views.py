from aiohttp_jinja2 import template
from aiohttp import web

from db import Endpoint, AccessLog, Response

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
            endpoint_t.select().where(endpoint_t.c.hash == hash_value))
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
        await conn.execute(
            accesslog_t.insert().values(access_data))
        return response_obj


async def create_endpoint(request):
    db = request.app['db']
    async with db.acquire() as conn:
        async with conn.begin():
            hash_value = str(uuid.uuid4())
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
        status_code = post_data.get('status_code', 200)
        try:
            headers = json.loads(post_data.get('headers'))
        except TypeError:
            headers = []
        response_body = post_data.get('response_body', '')
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
