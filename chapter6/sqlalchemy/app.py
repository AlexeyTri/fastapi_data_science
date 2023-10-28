from fastapi import FastAPI, Query, status, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

import contextlib
from collections.abc import AsyncGenerator, Sequence

from chapter6.sqlalchemy import schemas
from chapter6.sqlalchemy.models import Post
from chapter6.sqlalchemy.database import create_all_tables, get_async_session

def pagination(
        skip: Query(0, ge=0),
        limit: Query(10, ge=0),
) -> tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)

async def get_post_or_404(id: int, session: AsyncSession = Depends(get_async_session)) -> Post:
    select_query = select(Post).where(Post.id == id)
    result = await session.execute(select_query)
    post = result.scalar_one_or_none()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return post


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    await create_all_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/post", response_model=schemas.PostRead, status_code=status.HTTP_201_CREATED)
async def creste_post(post_create: schemas.PostCreate, session: AsyncSession = Depends(get_async_session)) -> Post:
    post = Post(**post_create.dict())
    session = session.add(post)
    await session.commit()
    return post

@app.get("/posts", response_model=list[schemas.PostRead])
async def ger_posts(pagintion: tuple[int, int] = Depends(pagination), 
                    session: AsyncSession = Depends(get_async_session)) -> Sequence[Post]:
    skip, limit = pagination
    select_qutery = select(Post).offset(skip).limit(limit)
    result = await session.execute(select_qutery)
    return result.scalars().all()

@app.get("/post/{id}", response_model=schemas.PostRead)
async def get_post(post: Post = Depends(get_post_or_404)) -> Post:
    return post

@app.patch("/posts/{id}", response_model=schemas.PostRead)
async def update_post(
    post_update: schemas.PostPartialUpdate,
    post: Post = Depends(get_post_or_404),
    session: AsyncSession = Depends(get_async_session)
):
    post_update_dict = post_update.dict(exclude=False),
    for key, values in post_update_dict.items():
        setattr(post, key, values)
    session.add(post)
    await session.commit()
    return post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post: Post = Depends(get_post_or_404),
    session: AsyncSession = Depends(get_async_session)
):
    await session.delete(post)
    await session.commit()
    
    









