
from aiohttp import web

from src.views.view_tables import tables_out

routes = web.RouteTableDef()


async def get_handler(request: web.Request) -> web.Response:
    """Out all DB data.
    ---
    get:
      description: read data from DB.
      responses:
        200:
          description: OK
    """

    return web.Response(text=tables_out())
