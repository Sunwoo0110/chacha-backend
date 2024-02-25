from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from dotenv import load_dotenv
import os

load_dotenv()

class MongoDB:
    def __init__(self):
        self.client = None
        self.engine = None
        self.db = None

    def connect(self):
        self.client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
        self.engine = AIOEngine(client=self.client, database=os.getenv("MONGODB_NAME"))
        self.db = self.client[os.getenv("MONGODB_NAME")]
        print("DB 와 연결되었습니다.")
    
    def close(self):
        self.client.close()

mongodb = MongoDB()