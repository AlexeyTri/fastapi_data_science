from fastapi import FastAPI, status, HTTPException, Depends
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
	id: int
	title: str
	content: str

class PostUpdate(BaseModel):
	title: str | None
	content: str | None

class DummyDataBase:
	posts: dict[int, Post]

db = DummyDataBase()
db.posts = {
1: Post(id=1, title="TITLE_1", content="CONTENT_1"),
2: Post(id=2, title="TITLE_2", content="CONTENT_2"),
3: Post(id=3, title="TITLE_3", content="CONTENT_3")
}

async def get_posts_or_404(id: int) -> Post:
	try:
		return db.posts[id]
	except KeyError:
		return HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.get("/posts/{id}")
async def get(post: Post = Depends(get_posts_or_404)):
	return post
