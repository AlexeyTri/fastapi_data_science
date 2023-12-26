from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from password import verify_password
from models import User, AccessToken

async def authentication(email: str, password: str, session: AsyncSession) -> User | None:
    query = select(User).where(User.email == email)
    result = await session.execute(query)
    user: User | None = result.scalar_one_or_none()

    if user is None:
        return None
    
    if not verify_password(password, user.hash_passward):
        return None
    
    return user

async def create_access_token(user: User, session: AsyncSession) -> AccessToken:
    access_token = AccessToken(user=user)
    session.add(access_token)
    await session.commit()
    return access_token