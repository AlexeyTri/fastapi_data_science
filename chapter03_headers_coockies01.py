from fastapi import FastAPI, Header, File, UploadFile

app = FastAPI()

@app.get("/")
async def get_headers(hello: str = Header(...)):
	return {"hello":hello}
