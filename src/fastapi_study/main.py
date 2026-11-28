from fastapi import FastAPI
from apps.app01 import app01
from apps.app02 import app02
from apps.app03 import app03

app = FastAPI()
app.include_router(app01,tags=["路径参数"])
app.include_router(app02,tags=["查询参数"])
app.include_router(app03,tags=["请求体参数"])


