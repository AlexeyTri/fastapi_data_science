from fastapi import FastAPI, Depends, Header, status, HTTPException, APIRouter

def secret_header(secret_header: str | None = Header(None)) -> None:
	if not secret_header or secret_header != "SECRET_VALUE":
	return HTTPException(status.HTTP_403_FORBIDDEN)

# 1 example: dependency in path decorator

@app.get("/protected-route", dependecies=[Depends(secret_header)])
async def protected_route():
	return {"hello": "world"}

# 2 example: dependency in router

router = APIRouter(dependecies=[Depends(secret_header)])
@router.get("/route1")
async def router_router1():
	return{"router": "router1"}
@router.get("/router2")
async def router_route2():
	return{"router":"router2"}

app = FastAPI()

app.include_router(router, prefix="/router")

# 3 example: global dependency

app = FastAPI(dependencies=[Depends(seret_header)])

@app.get("/route1")
	async def get_route1():
	return{"router": "route1"}

@app.get("/route2")
	async def get_route2():
	return{"route": "route2"}
