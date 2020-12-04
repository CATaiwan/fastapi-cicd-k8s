from fastapi import FastAPI, Request

from .routes.v1 import demo

app = FastAPI(title="Fastapi K8S Demo", description="", version="0.0.1", redoc_url=None)


@app.get("/")
def hello(request: Request):
    return {"hello": "world"}


app.include_router(demo.router, prefix="/api/v1/demo", tags=["Demo"])
