from fastapi import FastAPI, Depends

app = FastAPI()

def pagination(skip: int=0, limit: int=10) -> tuple[int, int]:
	return(skip, limit)

@app.get("/items")
async def list_limit(p: tuple[int, int] = Depends(pagination)):
	skip, limit = p
	return {"skip": skip, "limit":limit} 
