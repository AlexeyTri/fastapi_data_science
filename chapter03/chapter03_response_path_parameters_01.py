from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
	title: str

@app.post("/post", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
	return post
