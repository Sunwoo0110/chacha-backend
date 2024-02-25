from models import mongodb
from models.characters import Characters

class CharacterController:    
    async def create_character(self, character):        
        new_character = await mongodb.db.characters.insert_one(character)
        return new_character
    
    async def read_characters(self):
        character_list = []
        async for document in mongodb.db.characters.find({"open": True}):
            character_list.append(document)
        return character_list