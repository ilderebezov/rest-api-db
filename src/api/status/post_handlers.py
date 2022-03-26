
import datetime as dt

from aiohttp import web

from src.models import User
from src.models import Tariff
from src.models import Event

routes = web.RouteTableDef()


async def post_user(request: web.Request) -> web.Response:
    """
    Add new user data to DB table users.
    :param request:
    :return:
    """

    request = await request.json()
    User.get_or_create(user_id=int(request['user_id']),
                       balance=request['balance'],
                       data_adding=dt.datetime.strptime(request['data_adding'], '%Y-%m-%d'),
                       age=int(request['age']),
                       city_of_living=request['city_of_living'],
                       data_last_activity=dt.datetime.strptime(request['data_last_activity'], '%Y-%m-%d'),
                       current_tariff=int(request['current_tariff']),
                       )
    return web.Response(text='new user added ok')


async def post_tariff(request: web.Request) -> web.Response:
    """
    Add new tariff data to DB table tariffs.
    :param request:
    :return:
    """

    request = await request.json()
    Tariff.get_or_create(tariff_id=int(request['tariff_id']),
                         tariff_name=request['tariff_name'],
                         data_start=dt.datetime.strptime(request['data_start'], '%Y-%m-%d'),
                         data_end=dt.datetime.strptime(request['data_end'], '%Y-%m-%d'),
                         number_of_min=request['number_of_min'],
                         number_of_sms=request['number_of_sms'],
                         number_of_mb=request['number_of_mb'],
                         )
    return web.Response(text='new tariff added ok')


async def post_event(request: web.Request) -> web.Response:
    """
    Add new event data to DB table events.
    :param request:
    :return:
    """

    request = await request.json()
    Event.get_or_create(event_id=request['event_id'],
                        time_event=dt.datetime.strptime(request['time_event'], '%Y-%m-%d %H-%M-%S'),
                        user_id=request['user_id'],
                        service_type=request['service_type'],
                        units_spent=request['units_spent'],
                        )
    return web.Response(text='new event added ok')
