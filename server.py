from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import config
from . import db
from . import utils
from . import views
from . import ws
from . import ws_views
from . import ws_views_test
from . import ws_views_test2

app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)

# CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 初始化各个模块
ws.init_app(app)
ws_views.init_app(app)
ws_views_test.init_app(app)
ws_views_test2.init_app(app)
db.init_app(app)
utils.init_app(app)
views.init_app(app)
config.init_app(app)

# 首页路由
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
