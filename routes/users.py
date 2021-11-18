import sqlalchemy
from fastapi import APIRouter
from database.config import database, DATABASE_URL
from pydantic import BaseModel

# user model
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer),
    sqlalchemy.Column("name", sqlalchemy.String(255)),
    sqlalchemy.Column("email", sqlalchemy.String(255), primary_key=True)
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)


class User(BaseModel):
    id: int
    name: str
    email: str

    def insert(self):
        pass


router = APIRouter(
    prefix="/users"
)


@router.get("")
async def read_root():
    query = users.select()
    return await database.fetch_all(query)


@router.post("")
async def create_user(user: User):
    query = user.insert().vaclues(name=user.name, email=user.email)
    last_record_id = await database.execute(query)
    return {**query.dict(), "id": last_record_id}
