import argparse

from aiohttp import web
import aiohttp_jinja2

import jinja2

from pathlib import Path

from db import init_pg, close_pg
from routes import setup_routes
from utils import load_config, dict_merge


parser = argparse.ArgumentParser(description="endpoints server")
parser.add_argument('--port')


if __name__ == '__main__':
    app = web.Application()
    conf = load_config(str(Path('.') / 'config' / 'endpoints.yaml'))
    local_conf = load_config(str(Path('.') / 'config' / 'local.yaml'))
    if local_conf:
        dict_merge(conf, local_conf)
    app['config'] = conf
    app['sockets'] = {}
    aiohttp_jinja2.setup(
        app, loader=jinja2.FileSystemLoader('endpoints/templates/'))
    setup_routes(app=app)
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
    port = parser.parse_args().port
    if port is None:
        port = '8080'
    web.run_app(app, host='127.0.0.1', port=int(port))
