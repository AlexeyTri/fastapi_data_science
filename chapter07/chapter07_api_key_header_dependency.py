#create my dependency from token
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader

key_token = "SECURITY_KEY_TOKEN"

app = FastAPI()
security_token = APIKeyHeader(name="Token")


async def get_token(token: str = Depends(security_token)):
    if token != key_token:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    
@app.get("/protected_route", dependencies=[Depends(get_token)])
async def protected_route():
    return {"hello": "world"}