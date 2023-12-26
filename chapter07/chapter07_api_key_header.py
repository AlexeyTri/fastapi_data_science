#create ApiKeyHeader dependency enjction
from fastapi import Depends, status, FastAPI, HTTPException
from fastapi.security import APIKeyHeader

#наш пароль
API_TOKEN = "my_key_token"

app = FastAPI()
#заголовок ТОКЕН, именно его значение будет проверяться на соответствие с паролем
api_key_header = APIKeyHeader(name="Token")

@app.get("/protected_route")
async def get_protected_route(token: str = Depends(api_key_header)):
    if token != API_TOKEN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return {"hello": "world"}