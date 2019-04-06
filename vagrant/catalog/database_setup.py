from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    category = Column(String(250), nullable=False)
    created_on = Column(Date,nullable=False)
    last_updated_on = Column(Date)

engine = create_engine('sqlite:///itemcatalog.db')

Base.metadata.create_all(engine)