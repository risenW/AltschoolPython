from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from uuid import UUID
from schema import User, UserCreate, Response
from user_service import UserService
from utils import get_password_hash
from typing import Annotated
from api.dep import get_current_user

router = APIRouter()

users: list[User] = []


# Add users to the API
@router.post("/", status_code=status.HTTP_201_CREATED)
def add_user(user_in: UserCreate):
    user = User(
        id=str(UUID(int=len(users) + 1)),
        name=user_in.name,
        email=user_in.email,
        password=get_password_hash(user_in.password),
    )
    users.append(user)
    return Response(message="User added successfully", data=user)


# Password based authentication
@router.get("/me", status_code=status.HTTP_200_OK)
def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
