from fastapi import APIRouter

from ...services import FruitService


router = APIRouter()


@router.get("/apple/color")
async def color():
    service = FruitService()

    return {"color": service.get_apple_color()}
