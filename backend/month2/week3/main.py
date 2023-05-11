from typing import Annotated
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from schema import Response
from api.api import api_router
from user_service import UserService

app = FastAPI(
    title="Books API",
    description="A simple API to manage books in a library",
    version="1.0.0",
    docs_url="/api/v1/docs",
)

app.include_router(api_router)


@app.get("/", status_code=200)
def home():
    return Response(message="Hello from the books API")


@app.get("/token", status_code=status.HTTP_200_OK)
def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    email = form_data.username
    password = form_data.password

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

    return {"access_token": user.id, "token_type": "bearer"}
