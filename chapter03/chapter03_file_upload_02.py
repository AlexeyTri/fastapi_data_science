from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files")
async def upload_file(file: bytes = UploadFile(...)):
	return {"filename": file.name, "content":file.content}
