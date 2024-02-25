from models import mongodb
from models.users import Users
from bson import ObjectId

class UserController:    
    async def create_user(self, uuid):
        # existing_user = await mongodb.engine.find_one(Users, Users.uuid == uuid)
        existing_user = await mongodb.db.users.find_one({"uuid": uuid })
        if existing_user:
            # 기존 사용자가 있으면, 해당 사용자의 ID를 반환
            print(existing_user)
            return existing_user
        else:
            # 사용자가 없으면, 새로운 사용자를 추가
            new_user = await mongodb.db.users.insert_one({"uuid": uuid, "chat_cnt": 0 })
            find_user = await mongodb.db.users.find_one({"_id": ObjectId(new_user.inserted_id) })
            print(find_user)
            return find_user