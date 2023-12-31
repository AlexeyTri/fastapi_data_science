from fastapi import FastAPI, status, Response
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
	title: str
#	nb_views: int

posts = {1: Post(title="Hello", nb_views=100), 2: Post(title="Alex", nb_views=200)}

@app.put("/posts/{id}")
async def update_or_create(id: int, post: Post, response: Response):
	if id not in posts: 
		response.status_code = status.HTTP_201_CREATED
	posts[id] = post
	return posts[id]
