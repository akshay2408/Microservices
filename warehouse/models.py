from sqlalchemy import Column, Integer, String

from gateway.database import Base


class WareHouse(Base):
    __tablename__ = "warehouse"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    address = Column(String, index=True)
    city = Column(String, index=True)
    country = Column(String, index=True)
