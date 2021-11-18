import sqlalchemy
from fastapi import APIRouter
from database.config import database, DATABASE_URL
from pydantic import BaseModel

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


class Users(BaseModel):
    name: str
    email: str


router = APIRouter(
    prefix="/users"
)


@router.get("")
async def read_root():
    query = users.select()
    return await database.fetch_all(query)


@router.post("")
async def create_user(user: Users):
    query = users.insert().values(name=user.name, email=user.email)
    await database.execute(query)
    return {}
