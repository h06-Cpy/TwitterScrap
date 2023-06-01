from sqlalchemy import Column, Text, Integer, DateTime
from database import Base

class Tweet(Base):
    __tablename__ = 'tweet'

    id = Column(Integer, primary_key=True)
    tweetDate = Column(DateTime, nullable=False)
    createdDate = Column(DateTime, nullable=False)
    rawContent = Column(Text, nullable=False)
    renderedContent = Column(Text, nullable=False)
    lang = Column(Text, nullable=False)
    url = Column(Text, nullable=False)
    replyCount=Column(Integer, nullable=False)
    retweetCount= Column(Integer, nullable=False)
    likeCount= Column(Integer, nullable=False)
    quoteCount= Column(Integer, nullable=False)
    conversationId= Column(Integer, nullable=False)

    source= Column(Text, nullable=True)
    sourceUrl= Column(Text, nullable=True)
    sourceLabel= Column(Text, nullable=True)
    viewCount= Column(Integer, nullable=True)
    hashtags= Column(Text, nullable=True)

    companyName = Column(Text, nullable=False)