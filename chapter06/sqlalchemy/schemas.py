#schemas - модели Pydantic, необходимые для сериализации и валидации данных,
#а также для перемещения по базе данных


from datetime import datetime

from pydantic import BaseModel, Field

class CommentBase(BaseModel):
    publication_date: datetime = Field(default_factory=datetime.now)
    content: str

    class Config:
        orm_mode = True

class CommentCreate(CommentBase):
    pass


class CommentRead(CommentBase):
    id: int
    post_id: int




class PostBase(BaseModel):
    title: str
    content: str
    publication_date: datetime = Field(default_factory=datetime)

    class Config:
        orm_mode = True

class PostPartitialUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


class PostCreate(PostBase):
    id: int
    comments: list[CommentRead]


class PostRead(PostBase):
    id: int
    comment: list[CommentRead]


