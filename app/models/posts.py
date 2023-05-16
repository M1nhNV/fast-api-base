import sqlalchemy
import uuid

from database.config import database, DATABASE_URL
from app.requests.posts import PostsRequest

metadata = sqlalchemy.MetaData()

posts = sqlalchemy.Table(
    'posts',
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String)
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)


async def get_list():
    query = posts.select()
    return await database.fetch_all(query)


async def create_posts(post: PostsRequest):
    query = posts.insert().values(id=post.id, title=post.title)
    result = await database.execute(query)
    return result
