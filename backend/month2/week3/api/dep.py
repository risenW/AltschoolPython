from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends
from schema import User

# This is a dependency that will be used in the API routes
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user
