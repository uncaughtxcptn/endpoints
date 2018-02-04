from aiohttp import web

import json
import yaml

from db import Response

from sqlalchemy import desc


def load_config(fname):
    with open(fname, 'rt') as f:
        data = yaml.load(f)
    return data


statusCodeChoices = {
    100: 'Continue',
    101: 'Switching Protocols',
    102: 'Processing',
    103: 'Early Hints',

    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    203: 'Non-Authoritative Information',
    204: 'No Content',
    205: 'Reset Content',
    206: 'Partial Content',

    300: 'Multiple Choices',
    301: 'Moved Permanently',
    302: 'Found',
    303: 'See Other',
    304: 'Not Modified',
    305: 'Use Proxy',
    306: 'Switch Proxy',
    307: 'Temporary Redirect',
    308: 'Permanent Redirect',

    400: 'Bad Request',
    401: 'Unauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    406: 'Not Acceptable',
    407: 'Proxy Authentication Required',
    408: 'Request Timeout',
    409: 'Conflict',
    410: 'Gone',
    411: 'Length Required',
    412: 'Precondition Failed',
    413: 'Payload Too Large',
    414: 'URI Too Long',
    415: 'Unsupported Media Type',
    416: 'Range Not Satisfiable',
    417: 'Expectation Failed',
    418: 'I\'m a teapot',
    421: 'Misdirected Request',
    426: 'Upgrade Required',
    428: 'Precondition Required',
    429: 'Too Many Requests',
    431: 'Request Header Fields Too Large',
    451: 'Unavailable For Legal Reasons',

    500: 'Internal Server Error',
    501: 'Not Implemented',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'HTTP Version Not Supported',
    506: 'Variant Also Negotiates',
    510: 'Not Extended',
    511: 'Network Authentication Required',
}


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

    response_text = 'HTTP/1.1 {status} {message}'.format(
        status=response_obj.status,
        message=statusCodeChoices[response_obj.status])
    for header in response_obj.headers:
        response_text += '\n{}: {}'.format(
            header, response_obj.headers[header])
    response_text += '\n\n{}'.format(response_obj.text)
    return response_obj, response_text
