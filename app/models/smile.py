import uuid
from pydantic import BaseModel
from sqlalchemy import Column, String
from database import Base

class Smile(Base):
    __tablename__ = "smiles"
    id = Column(String, primary_key=True, index=True)
    component = Column(String, index=True)