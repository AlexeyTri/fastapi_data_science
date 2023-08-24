#!/Users/alexeylitovchenko/fastapi-data-science/ENV_DIR/bin/python

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def hello_world():
	return{"Hello": "World"}

@app.get("/users/{type}/{id}")
async def get_users(type: str, id: int):
	return{"type": type, "id": id}

