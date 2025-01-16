from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blog = relationship('Blog',back_populates='creator')


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer,primary_key=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer,ForeignKey('users.id'))

    creator = relationship('User',back_populates='blog')
