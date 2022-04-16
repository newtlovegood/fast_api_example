from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from . import models, schemas
from .db import engine
from .api.api import api_router

models.Base.metadata.create_all(bind=engine)  # usually ALEMBIC is used for this purpose + migrations

app = FastAPI()

templates = Jinja2Templates(directory='app/templates')


@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    context = {
        'request': request,
    }
    return templates.TemplateResponse('home.html', context)


app.include_router(api_router)
