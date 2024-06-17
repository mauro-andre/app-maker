from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse
from starlette.requests import Request


async def index(req: Request):
    return JSONResponse({"Hello": "World"})


routes = [Route("/", endpoint=index)]


class AppMaker(Starlette):
    def __init__(self, routes: list = [Route("/", endpoint=index)], **kwargs):
        super().__init__(routes=routes, **kwargs)
