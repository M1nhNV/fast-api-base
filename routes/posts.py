from fastapi import APIRouter
from app.controllers.posts import index, create_a_post
from app.requests.posts import PostsRequest

router = APIRouter(
    prefix="/posts"
)


@router.get("")
async def read_root():
    return await index()


@router.post("")
async def create(post: PostsRequest):
    ref = await create_a_post(post)
    return ref
