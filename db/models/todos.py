import uuid

from sqlalchemy import Boolean, Column, Integer, String
from db.models.base_model import Base
 
class Todos(Base):
    __tablename__ = "todos"
 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    complete = Column(Boolean, default=False)