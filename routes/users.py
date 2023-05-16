from fastapi import APIRouter
from app.controllers.users import index, create_a_user
from app.requests.user import Users

router = APIRouter(
    prefix="/users"
)


@router.get("")
async def read_root():
    return await index()


@router.post("")
async def create(user: Users):
    rs = await create_a_user(user)
    return rs
