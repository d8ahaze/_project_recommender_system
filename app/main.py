# Запуск сервера:
# python -m uvicorn app.main:app --port 8000 --reload
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .library.auxiliary import *
from app.routers import router_unsplash


app = FastAPI()

templates = Jinja2Templates(directory='templates')

app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(router_unsplash.router)


@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    """Если запрашивается корень проекта - вернёт на фронт: page.html; further using: объект запроса
    и данные, отправляемые на фронт"""
    data = openfile('home.md')
    return templates.TemplateResponse('page.html', {'request': request, 'data': data})


@app.get('/page/{page_name}', response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    """Если запрашивается /page/any - вернёт на фронт: page.html; further using: объект запроса
    и имя страницы"""
    data = openfile(page_name+'.md')
    return templates.TemplateResponse('page.html', {'request': request, 'data': data})
