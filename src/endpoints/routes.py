from views import (index, create_endpoint, visit_endpoint, view_access_logs,
                   set_response_data, get_auto_response, sockets,
                   EndpointLiveView)

from pathlib import Path


def setup_routes(app):
    app.router.add_route('GET', '/', index, name='home')
    app.router.add_get('/endpoints', create_endpoint)
    app.router.add_get('/endpoints/list', index)
    app.router.add_route('*', '/{hash}', visit_endpoint)
    app.router.add_get('/{hash}/view', index)
    app.router.add_get('/{hash}/logs', view_access_logs)
    app.router.add_post('/{hash}/response', set_response_data)
    app.router.add_get('/{hash}/auto-response', get_auto_response)
    app.router.add_route('*', '/{hash}/live', EndpointLiveView)
    app.router.add_get('/{hash}/ws', sockets)
    if app['config']['debug']:
        app.router.add_static(
            '/static/', path=str(Path('..') / 'static'), name='static')
