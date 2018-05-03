import logging;logging.basicConfig(level=logging.INFO)  # 设置logging，还可以配置日志文件，日志格式等
import asyncio
from aiohttp import web


def index(request):
    return web.Response(body='<html><h1>okkkk</h1></html>', content_type='text/html')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
