from aiohttp_jinja2 import template
from aiohttp import web

from db import Endpoint

import uuid


@template('index.html')
async def index(request):
    pass


async def create_endpoint(request):
    db = request.app['db']
    async with db.acquire() as conn:
        async with conn.begin():
            hash_value = str(uuid.uuid4())
            data = await conn.execute(
                Endpoint.__table__.insert().values({'hash': hash_value}))
            data = await data.fetchone()
    return web.json_response({'id': data.id, 'hash': hash_value})
