import sqlalchemy
from database.config import database, DATABASE_URL
from app.requests.user import Users
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String, primary_key=True)
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)


async def get_list():
    query = users.select()
    return await database.fetch_all(query)


async def create_user(user: Users):
    query = users.insert().values(name=user.name, email=user.email)
    result = await database.execute(query)
    return result
