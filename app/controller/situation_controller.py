from models import mongodb
from models.situations import Situations

class SituationController:    
    async def create_situation(self, situation):        
        new_situation = await mongodb.db.situations.insert_one(situation)
        return new_situation