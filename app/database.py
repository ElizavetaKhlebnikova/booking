from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings

engine = create_async_engine(settings.DATABASE_URL)

# генератор сессий используется для проведения транзакций
# expire_on_commit=False - позволяет не прекращать работу с бд после коммита
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Base используется для миграций (в ней аккумулируются данные из моделей-наследников)
class Base(DeclarativeBase):
    pass
