from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from .page import Page


class AppMaker(Starlette):
    def __init__(self, pages: list[Page], **kwargs):
        self.pages = pages
        self._templates = Jinja2Templates(directory="app_maker/templates")
        self._routes = []
        self._init_pages()
        super().__init__(routes=self._routes, **kwargs)

    async def _index(self, req: Request, context):
        return self._templates.TemplateResponse(
            request=req, name="index.html", context=context
        )

    def _index_factory(self, context: dict):
        async def endpoint(req: Request):
            return await self._index(req=req, context=context)

        return endpoint

    def _init_pages(self):
        for page in self.pages:
            context = {"page_title": page.title}
            self._routes.append(
                Route(path=page.path, endpoint=self._index_factory(context=context))
            )
