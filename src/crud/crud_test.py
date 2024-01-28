from sqlalchemy.orm import Session
from database.models.test_model import Test

def get_items(db: Session):
    return db.query(Test).all()