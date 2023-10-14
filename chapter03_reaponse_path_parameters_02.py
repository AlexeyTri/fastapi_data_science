from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
	title: str
	nb_views: int

post = {1: Post(title="Hello", nb_views=100), 2: Post(title="Alex", nb_views=200)}

@app.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
	post.pop(id, None)
	return None
