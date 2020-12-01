from fastapi import APIRouter

from ...services import DemoService


router = APIRouter()


@router.get("/")
async def index():
    return {"message": "Demo Index"}


@router.get("/color")
async def color():
    service = DemoService()
    return {"color": service.color()}
