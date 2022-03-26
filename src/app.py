from aiohttp import web
from src.service import routes


def app_init():
    service = web.Application()
    routes.setup_routes(service)
    web.run_app(service, host='0.0.0.0', port=8080)
