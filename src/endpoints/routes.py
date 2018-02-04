from views import index, create_endpoint

from pathlib import Path


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/endpoint', create_endpoint)
    app.router.add_get('/{hash}', index)
    app.router.add_static(
        '/static/', path=str(Path('.') / 'static'), name='static')
