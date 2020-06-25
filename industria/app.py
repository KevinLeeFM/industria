from pathlib import Path
from importlib import resources
from os import chdir
import os.path

from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse
from starlette.routing import Route, Mount
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

pkgpath = Path(os.path.dirname(__file__))

templates = Jinja2Templates(directory=pkgpath/'resources/templates')

async def homepage(request):
    return templates.TemplateResponse('index.html', 
        {
            'request': request,

            'user': {
                'name': 'Kevin'
            }
        }
    )

async def api(request):
    pass

app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/api', api),
    Mount('/static', app=StaticFiles(directory=pkgpath/'resources/statics'), name='static')
])