from fastapi import APIRouter, status, HTTPException
from uuid import UUID
from schema import User, UserCreate, Response
from user_service import UserService
from utils import get_password_hash

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
@router.get("/login", status_code=status.HTTP_200_OK)
def login_user(email: str, password: str):
    user_service = UserService(users)
    user = user_service.find_user_by_email(email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    if not user_service.check_password(email, password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password"
        )

    return Response(message="User logged in successfully", data=user)
