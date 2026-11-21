from sqlalchemy import Column, Integer, String, Text
from .database import Base

class AIRequest(Base):
    __tablename__ = "ai_requests"

    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(Text, nullable=False)
    generated_text = Column(Text, nullable=False)