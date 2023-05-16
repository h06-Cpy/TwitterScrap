from sqlalchemy import Column, Text, Integer
from database import Base

class Tweet(Base):
    __tablename__ = 'tweet'

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)