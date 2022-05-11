from sqlalchemy import Column, Integer, String

from gateway.database import Base


class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    sales_type = Column(String, unique=True, index=True)
    sales_market = Column(String, index=True)
