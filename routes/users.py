from fastapi import APIRouter
from app.controllers.users import index

router = APIRouter(
    prefix="/users"
)


@router.get("")
async def read_root():
    return index()
