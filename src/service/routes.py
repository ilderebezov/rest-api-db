import aiohttp_cors
from aiohttp.web_app import Application

from src.api.status.get_handlers import get_handler
from src.api.status.post_handlers import post_user
from src.api.status.post_handlers import post_tariff
from src.api.status.post_handlers import post_event
from src.api.status.del_hendlers import del_user
from src.api.status.del_hendlers import del_tariff
from src.api.status.del_hendlers import del_event
from src.api.status.put_heandlers import put_user
from src.api.status.put_heandlers import put_tariff
from src.api.status.put_heandlers import put_event


def setup_routes(app: Application):
    """Настраивает эндпоинты сервиса с поддержкой CORS."""
    cors = aiohttp_cors.setup(app, defaults={
        '*': aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers='*',
            allow_headers='*',
        ),
    })

    cors.add(app.router.add_get('/', get_handler))
    cors.add(app.router.add_post('/user', post_user))
    cors.add(app.router.add_post('/tariff', post_tariff))
    cors.add(app.router.add_post('/event', post_event))
    cors.add(app.router.add_delete('/user_del', del_user))
    cors.add(app.router.add_delete('/tariff_del', del_tariff))
    cors.add(app.router.add_delete('/event_del', del_event))
    cors.add(app.router.add_put('/user_update', put_user))
    cors.add(app.router.add_put('/tariff_update', put_tariff))
    cors.add(app.router.add_put('/event_update', put_event))
