#создана база данных - models
#создана схема подключения к базе - schemas
#создадим подключение нашего приложения к базе - database

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from sqlalchemy.models import Base

DATABASE_URL = "sqlite+aiosqlite:///chapter06_sqlalchemy.db"

#объявляем движек, устанавливающий связь с базой данных
engine = create_async_engine(DATABASE_URL)

#создадим функцию, генерирующую сеансы связи с базой данных
#session - это аналог индекса в GIT 
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

#при выполнении запроса HTTP сервер открывается, после выполнения запроса он закрывается
#для выполнения этого условия, сформируем нижеприведенную функцию, которую далее будем использовать как зависимость
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def create_all_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)