from fastapi import FastAPI, status, HTTPException, Depends, Query
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

#async def get_posts_or_404(id: int) -> Post:
#	try:
#		return db.posts[id]
#	except KeyError:
#		return HTTPException(status_code=status.HTTP_404_NOT_FOUND)

##@app.get("/posts/{id}")
#async def get(post: Post = Depends(get_posts_or_404)):
#	return post


class Pagination():
	def __init__(self, maximum_limit: int = 100):
		self.maximum_limit = maximum_limit
	async def __call__(self,
			skip: int = Query(0, ge=0),
			limit: int = Query(10, ge=0)) -> tuple[int, int]:
		called_limit = min(self.maximum_limit, limit)
		return (skip, called_limit)

pagination = Pagination(maximum_limit=50)

@app.get("/items")
async def get_page(p: tuple[int, int] = Depends(pagination)):
	skip, limit = p
	return {"skip": skip, "limit": limit}

























