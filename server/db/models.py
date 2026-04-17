from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    doctor = Column(String(100))
    notes = Column(Text)
    sentiment = Column(String(50))