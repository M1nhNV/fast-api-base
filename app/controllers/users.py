from app.entities.user import Users
from app.models.user import get_list


async def index():
    return await get_list()


async def create_user(user: Users):
    return {'code': 200, 'body': user}


class UsersControllers:
    def __init__(self):
        pass
