from fastapi import FastAPI, status, Request, Body, HTTPException

app = FastAPI()

@app.post("/password")
async def check_password(password: str = Body(...), password_comfirm: str = Body(...)):
	if password != password_comfirm:
		raise HTTPException(
			status.HTTP_400_BAD_REQUEST,
			detail={
				"message": "Password don't match.", 
				"hints": ["Check the Capslock buttom", "Try to write password with eye acon"]})
	return {"message": "Password match."}
