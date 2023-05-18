from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    first_name: str
    last_name: str
    dob: datetime
    address: str
    email: EmailStr


class UserCreate(UserBase):
    password: str
    pass


class UserUpdate(BaseModel):
    first_name: str = None
    last_name: str = None
    dob: datetime = None
    address: str = None
    email: EmailStr = None


class User(UserBase):
    id: str
    password: str
    created_at: datetime
    updated_at: datetime
