from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url='sqlite:///./tweet.db'

engine = create_engine(db_url)
Session = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()
