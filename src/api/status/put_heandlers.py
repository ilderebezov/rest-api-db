from aiohttp import web

from src.models import User
from src.models import Tariff
from src.models import Event
from sql import session
import datetime as dt

routes = web.RouteTableDef()


async def put_user(request: web.Request) -> web.Response:
    """
    Update user data in DB table users.
    :param request:
    :return:
    """

    request = await request.json()
    session.query(User).filter(User.User_Id == request['user_id']).\
        update({'Balance': request['balance'],
                'Data_adding': dt.datetime.strptime(request['data_adding'], '%Y-%m-%d'),
                'Age': int(request['age']),
                'City_of_living': request['city_of_living'],
                'Data_last_activity': dt.datetime.strptime(request['data_last_activity'], '%Y-%m-%d'),
                'Current_tariff': int(request['current_tariff'])
                })
    session.commit()
    return web.Response(text='user update Ok')


async def put_tariff(request: web.Request) -> web.Response:
    """
    Update tariff data in DB table tarifs.
    :param request:
    :return:
    """

    request = await request.json()
    session.query(Tariff).filter(Tariff.Tariff_id == request['tariff_id']).\
        update({'Tariff_name': request['tariff_name'],
                'Data_start': dt.datetime.strptime(request['data_start'], '%Y-%m-%d'),
                'Data_end': dt.datetime.strptime(request['data_end'], '%Y-%m-%d'),
                'Number_of_min': request['number_of_min'],
                'Number_of_sms': request['number_of_sms'],
                'Number_of_Mb': request['number_of_mb'],
                })
    session.commit()
    return web.Response(text='user update Ok')


async def put_event(request: web.Request) -> web.Response:
    """
    Update event data in DB table events.
    :param request:
    :return:
    """

    request = await request.json()
    session.query(Event).filter(Event.Event_id == request['event_id']).\
        update({'Time_event': dt.datetime.strptime(request['time_event'], '%Y-%m-%d %H-%M-%S'),
                'User_id': request['user_id'],
                'Service_type': request['service_type'],
                'Units_spent': request['units_spent'],
                })
    session.commit()
    return web.Response(text='user update Ok')