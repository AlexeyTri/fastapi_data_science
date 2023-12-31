from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/path")
async def get_request_object(request: Request):
	return {"path": request.url.path}
