from fastapi import FastAPI, Header, File, UploadFile

app = FastAPI()

@app.get("/")
async def get_headers(user_agent: str = Header(...)):
	return {"user_agent":user_agent}
