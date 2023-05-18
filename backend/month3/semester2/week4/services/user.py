from schemas.user import UserCreate, User
from database import users_collection
from datetime import datetime
from bson.objectid import ObjectId
from serializers import user_serializer
from fastapi.encoders import jsonable_encoder
from utils import get_password_hash


class UserService:
    def create_user(self, user_in: UserCreate):
        user_dict = user_in.dict()
        user_dict["password"] = get_password_hash(user_dict["password"])
        user = User(
            **user_dict, created_at=datetime.utcnow(), updated_at=datetime.utcnow()
        )
        user_id = users_collection.insert_one(jsonable_encoder(user)).inserted_id
        new_user = users_collection.find_one({"_id": user_id})

        return user_serializer(new_user)


user_service = UserService()
