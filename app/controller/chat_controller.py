from models import mongodb
from models.chats import Chats
from ai.Custom import Custom
from ai.Custom2 import Custom2
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo

class ChatController:    
    async def create_chat(self, chat):
        ## 답변 생성
        try:
            character = await mongodb.db.characters.find_one({"_id": ObjectId(chat.character_id)})
            # print(character)
            if not character:
                return None 
            
            if character["personality"] != "":
                custom = Custom(name=character["name"], intro=character["description"], set=character["setting"], 
                                personality=character["personality"], line=character["example_conv"])
            else:
                custom = Custom2(name=character["name"], intro=character["description"], set=character["setting"], 
                                line=character["example_conv"])
            # print(custom)
            response = await custom.receive_chat(chat.user_chat, chat.user_id)
            # print(response)
            ## 대화 저장
            new_chat = await mongodb.db.chats.insert_one({"user_id": chat.user_id, "character_id": chat.character_id, 
                                                          "user_chat": chat.user_chat, "ai_chat": response,
                                                          "created_at": datetime.now(ZoneInfo("Asia/Seoul"))})
            ## 캐릭터 채팅 횟수 증가
            await mongodb.db.characters.update_one({"_id": ObjectId(chat.character_id)}, {"$inc": {"chat_cnt": 1}})
            
            ## 사용자의 채팅 횟수 증가
            user = await mongodb.db.users.find_one({"_id": ObjectId(chat.user_id)})
            await mongodb.db.users.update_one({"_id": ObjectId(chat.user_id)}, {"$set": {"chat_cnt": user["chat_cnt"]+1}})
            
            return character["name"], character["img"], response, user["chat_cnt"]+1
        except:
            user = await mongodb.db.users.find_one({"_id": ObjectId(chat.user_id)})
            return character["name"], character["img"], "error", user["chat_cnt"]
    
    async def update_chat_cnt(self, character_id):
        character = await mongodb.db.characters.find_one({"_id": ObjectId(character_id)})
        await mongodb.db.characters.update_one({"_id": ObjectId(character_id)}, {"$inc": {"user_cnt": 1}})
        return character["user_cnt"]+1
    
    async def read_chats(self, user_id, character_id):
        chat_list = []
        character = await mongodb.db.characters.find_one({"_id": ObjectId(character_id)})
        async for document in mongodb.db.chats.find({"user_id": user_id, "character_id": character_id}):
            # print(document)
            chat_list.append({"name": character["name"], "img": character["img"], 
                             "user_chat": document["user_chat"], "ai_chat": document["ai_chat"]})
            
        if not chat_list:
            return "empty"
        return chat_list