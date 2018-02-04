from aiohttp import web

import json
import yaml

from db import Response

from sqlalchemy import desc


def load_config(fname):
    with open(fname, 'rt') as f:
        data = yaml.load(f)
    return data


async def get_http_request_string(request):
    request_text = '{method} {url} HTTP/{major}.{minor}'.format(
        method=request.method, url=request.rel_url,
        major=request.version.major, minor=request.version.minor)
    for header in request.raw_headers:
        request_text += '\n{}: {}'.format(
            str(header[0], 'utf-8'), str(header[1], 'utf-8'))
    request_text += '\n'
    reader = request.content
    content = await reader.read()
    request_text += '\n{}'.format(str(content, 'utf-8'))
    return request_text


async def get_response_data(endpoint, conn):
    response_t = Response.__table__
    result = await conn.execute(
        response_t.select().where(response_t.c.endpoint_id == endpoint.id).
        order_by(desc(response_t.c.id)))
    response = await result.first()
    if response is None:
        response_obj = web.Response(text='')
    else:
        headers = json.loads(response.headers)
        response_obj = web.Response(
            status=response.status_code, headers=headers, text=response.body)

    response_text = 'HTTP/1.1 {status}'.format(status=response_obj.status)
    for header in response_obj.headers:
        response_text += '\n{}: {}'.format(
            header, response_obj.headers[header])
    response_text += '\n\n{}'.format(response_obj.text)
    return response_obj, response_text
