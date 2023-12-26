import secrets
from datetime import datetime, timezone, timedelta
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, DateTime


def get_exparation_date(duration_seconds: int = 84600) -> datetime:
    return datetime.now(tz=timezone.utc) + timedelta(seconds=duration_seconds)

def generate_token() -> str:
    return secrets.token_urlsafe(32)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(1024), index=True, unique=True, nullable=False)
    hash_passward: Mapped[str] = mapped_column(String(1024), nullable=False)


class AccessToken(Base):
    __tablename__ = "access_token"
    access_token: Mapped[str] = mapped_column(String(1024), primary_key=True, default=generate_token)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    exparation_date: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=get_exparation_date)
    user: Mapped[User] = relationship("User", lazy="joined")



