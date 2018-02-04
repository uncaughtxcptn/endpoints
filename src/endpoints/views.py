from aiohttp_jinja2 import template
from aiohttp import web

from db import Endpoint, AccessLog

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
