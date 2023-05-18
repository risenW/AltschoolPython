from fastapi import APIRouter


accounts_router = APIRouter()


@accounts_router.get("/")
def get_all_accounts():
    pass
