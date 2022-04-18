import logging 
import logging.config
from time import asctime
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from . import models, schemas
from .config import settings
from .db import engine
from .api.api import api_router
from app.auth.api import auth_router


# setup loggers
logging.basicConfig(filename='logs.log', level=logging.INFO,
                    format="%(asctime)s loglevel=%(levelname)-6s logger=%(name)s %(funcName)s() L%(lineno)-4d %(message)s   call_trace=%(pathname)s L%(lineno)-4d"
)

# get root logger
# logger = logging.getLogger(__name__)

models.Base.metadata.create_all(bind=engine)  # usually ALEMBIC is used for this purpose + migrations

app = FastAPI()

templates = Jinja2Templates(directory='app/templates')


@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    logging.info('test')
    context = {
        'request': request,
    }
    return templates.TemplateResponse('home.html', context)


app.include_router(api_router)
app.include_router(auth_router)
