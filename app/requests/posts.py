from pydantic import BaseModel


class PostsRequest(BaseModel):
    id: str
    title: str

