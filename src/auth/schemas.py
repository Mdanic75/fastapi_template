from pydantic import BaseModel, EmailStr
import datetime


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr


class UserOut(UserBase):
    id: int
    last_login: datetime.datetime = None
    date_joined: datetime.datetime
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True


class UserIn(UserBase):
    password: str

    class Config:
        orm_mode = True


class GroupSchema(BaseModel):
    id: int
    name: str
    description: str = None

    class Config:
        orm_mode = True


class PermissionSchema(BaseModel):
    id: int
    name: str
    code_name: str

    class Config:
        orm_mode = True
