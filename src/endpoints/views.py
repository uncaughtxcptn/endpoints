from aiohttp import web

async def index(request):
    return web.Response(text='Hello World')