from app.requests.user import Users
from app.models.user import get_list, create_user


async def index():
    return await get_list()


async def create_a_user(user: Users):
    return await create_user(user)


class UsersControllers:
    def __init__(self):
        pass
