from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
async def get_response(response: Response):
	response.headers["Custom_headers"] = "Custom_hesders_value"
	return {"Hello": "world"}
