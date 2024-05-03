from models import mongodb
from models.characters import Characters
from bson import ObjectId

class CharacterController:    
    async def create_character(self, character):       
        new_character = await mongodb.db.characters.insert_one(character)
        return new_character
    
    async def read_characters(self, category):
        character_list = []
        async for document in mongodb.db.characters.find({"open": True, "category": category}).sort("user_cnt", -1):
            character_list.append(document)
            
        if not character_list:
            return "empty"
        return character_list
    
    async def read_character(self, character_id):
        character = await mongodb.db.characters.find_one({"_id": ObjectId(character_id)})
        return character