from fastapi import APIRouter, HTTPException, Depends
from schemas.account import AccountCreate
from services.account import account_service
from deps import get_current_user

accounts_router = APIRouter()


@accounts_router.get("/")
def get_all_accounts():
    pass


@accounts_router.post("/")
def create_account(account_in: AccountCreate, current_user=Depends(get_current_user)):
    account = account_service.create_account(account_in, current_user)

    if not account:
        raise HTTPException(
            status_code=401,
            detail={"message": "An error occurred when creating your account"},
        )

    return {"message": "Account created successfully!", "data": account}
