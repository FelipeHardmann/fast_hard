from sqlalchemy import Column, Integer, String
from app.config.database import Base

class ExampleModel(Base):
    __tablename__ = "examples"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
