import uuid

from sqlalchemy import Boolean, Column, UUID, String
from db.models.base_model import Base
 
class Todos(Base):
    __tablename__ = "todos"
 
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    complete = Column(Boolean, default=False)