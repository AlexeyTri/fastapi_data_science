from fastapi import FastAPI, Path, Body
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
	name: str
	age: int

@app.post("/users")
async def create_user(user: User, company: str = Body(...)):
	return {"user": user, "company": company}
