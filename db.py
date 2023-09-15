from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class RedditPost(Base):
    """_SQL Entity to store scraped reddit posts_

    Args:
    
    """
    __tablename__ = 'reddit_posts'
    id = Column(String, primary_key=True)
    title = Column(String)
    url = Column(String)
    content = Column(Text)
    created_utc = Column(DateTime)
    

engine = create_engine('sqlite:///reddit_data.db')

Base.metadata.create_all(engine)


def store_data(submission):
    Session = sessionmaker(bind = engine)
    session = Session()
    dt_object = datetime.fromtimestamp(submission.created_utc)    
    try:
        post = RedditPost(id = submission.id, title = submission.title, url = submission.url, content = submission.selftext, created_utc = dt_object)
        # Add and commit
        session.add(post)
        session.commit()
    
    except Exception as e:
        print(f"Error while storing data: {e}")
    finally:
        session.close()
        
