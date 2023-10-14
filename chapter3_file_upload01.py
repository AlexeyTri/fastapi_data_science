from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files")
async def upload_file(file: UploadFile = File(...)):
	return {"filename": file.filename, "content":file.content_type}
