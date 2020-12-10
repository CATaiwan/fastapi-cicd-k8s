from fastapi import FastAPI, Request

from . import __version__
from .routes.v1 import fruit

app = FastAPI(
    title="Fastapi K8S Demo", description="", version=__version__, redoc_url=None
)


@app.get("/")
def hello(request: Request):
    return {"hello": "world"}


app.include_router(fruit.router, prefix="/api/v1/fruit", tags=["Fruit"])
