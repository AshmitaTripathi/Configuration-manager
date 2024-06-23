from sqlalchemy import Column, Integer, String
from .database import Base

class Configuration(Base):
    __tablename__ = "configurations"
    id = Column(Integer, primary_key=True)
    country_code = Column(String, unique=True)
    business_name = Column(String)
    pan = Column(String)
    gstin = Column(String)
    