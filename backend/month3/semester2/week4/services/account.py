from schemas.account import AccountCreate, Account
from schemas.user import UserInDB
from database import accounts_collection
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from serializers import account_serializer


class AccountService:
    def create_account(self, account_in: AccountCreate, current_user: UserInDB):
        account_schema = Account(
            **account_in.dict(),
            user_id=current_user.id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        account_id = accounts_collection.insert_one(
            jsonable_encoder(account_schema)
        ).inserted_id
        account = accounts_collection.find_one({"_id": account_id})

        return account_serializer(account)


account_service = AccountService()
