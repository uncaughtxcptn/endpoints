from aiohttp import web

from routes import setup_routes


app = web.Application()
setup_routes(app=app)
web.run_app(app, host='127.0.0.1', port=8080)
