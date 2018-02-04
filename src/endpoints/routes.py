from views import index, create_endpoint, visit_endpoint

from pathlib import Path


def setup_routes(app):
    app.router.add_route('GET', '/', index, name='home')
    app.router.add_get('/endpoint', create_endpoint)
    app.router.add_get('/{hash}', visit_endpoint)
    app.router.add_static(
        '/static/', path=str(Path('.') / 'static'), name='static')
