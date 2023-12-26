import secrets
from datetime import datetime, timezone, timedelta

from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase

def get_exparetion_date(duration_seconds: int = 86400) -> datetime:
    return datetime.now(tz=timezone.utc) + timedelta(seconds=duration_seconds)

def generate_token() -> str:
    return secrets.token_urlsafe(32)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(1024), nullable=False, index=True, unique=True)
    hash_password: Mapped[str] = mapped_column(String(1024), nullable=False)

class AccessToken(Base):
    __tablename__ = "access_tokens"
    access_token: Mapped[str] = mapped_column(String(1024), default=generate_token, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    experation_date: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=get_exparetion_date)
    user: Mapped[User] = relationship("User", lazy="joined")

    def max_age(self) -> int:
        delta = self.experation_date - datetime.now(tz=timezone.utc)
        return int(delta.total_seconds())
    
    