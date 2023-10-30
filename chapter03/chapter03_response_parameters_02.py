from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
async def get_response(response: Response):
	response.set_cookie("cooekie-name", "cookies-value", max_age=86400, )
	return {"Hello": "world"}
