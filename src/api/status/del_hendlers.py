from aiohttp import web

from src.models import User
from src.models import Tariff
from src.models import Event
from sql import session

routes = web.RouteTableDef()


async def del_user(request: web.Request) -> web.Response:
    """
    Delete user data from DB table users.
    :param request:
    :return:
    """

    request = await request.text()
    session.query(User).filter(User.Id == request).delete()
    session.commit()
    return web.Response(text='user delete Ok')


@routes.delete('/tariff_del')
async def del_tariff(request: web.Request) -> web.Response:
    """
    Delete tariff data from DB table tariffs.
    :param request:
    :return:
    """

    request = await request.text()
    session.query(Tariff).filter(Tariff.Id == request).delete()
    session.commit()
    return web.Response(text='tariff delete Ok')


@routes.delete('/event_del')
async def del_event(request: web.Request) -> web.Response:
    """
    Delete event data from DB table tariffs.
    :param request:
    :return:
    """

    request = await request.text()
    session.query(Event).filter(Event.Id == request).delete()
    session.commit()
    return web.Response(text='event delete Ok')
