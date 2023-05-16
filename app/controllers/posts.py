from app.models.posts import get_list, create_posts
from app.requests.posts import PostsRequest
import uuid


async def index():
    return await get_list()


async def create_a_post(post: PostsRequest):
    post.id = uuid.uuid4()
    return await create_posts(post)


class UsersControllers:
    def __init__(self):
        pass
