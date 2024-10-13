from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Noun(Base):
    __tablename__ = 'nouns'
    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String, nullable=False)

class Verb(Base):
    __tablename__ = 'verbs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String, nullable=False)

class Adjective(Base):
    __tablename__ = 'adjectives'
    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String, nullable=False)
