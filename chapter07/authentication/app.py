import contextlib
from datetime import datetime, timezone
from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from database import create_all_tables, get_assync_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import exc, select
from password import get_password_hash, verify_password
from models import User, AccessToken
from authentication import authentication, create_access_token
import schemas

app = FastAPI()

async def get_current_user(
        token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token")),
        session: AsyncSession = Depends(get_assync_session)) -> User:
    
    query = select(AccessToken).where(AccessToken.access_token == token,
                                      AccessToken.exparation_date >= datetime.now(tz=timezone.utc))
    result = await session.execute(query)
    access_token: AccessToken | None = result.scalar_one_or_none()

    if access_token in None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    return access_token

    

@app.post("/register", status_code=status.HTTP_201_CREATED, response_model=schemas.UserRead)
async def register(
    user_create: schemas.UserCreate,
    session: AsyncSession = Depends(get_assync_session)) -> User:
    hashed_password = get_password_hash(user_create.passward)
    user = User(*user_create.dict(exclude={"password"}), hashed_password=hashed_password)
    try:
        session.add(user)
        await session.commit()
    except exc.IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    return user

@app.post("/token")
async def create_token(form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
                       session: AsyncSession = Depends(get_assync_session)):
    email = form_data.username
    password = form_data.password
    user = await authentication(email=email, password=password, session=session)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    token = await create_access_token(user, session)
    return {"access_token": token.access_token, "token_type": "bearer"}

@app.get("/protected-route", response_model=schemas.UserRead)
async def protected_route(user: User = Depends(get_current_user)):
    return user