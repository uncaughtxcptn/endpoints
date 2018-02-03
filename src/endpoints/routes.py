from views import index

from pathlib import Path


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_static(
        '/static/', path=str(Path('.') / 'static'), name='static')
