from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    class Config:
        orm_mode = True


class UserCreate(UserBase):
    passward: str


class User(UserBase):
    id: int
    hash_passward: str


class UserRead(UserBase):
    id: int