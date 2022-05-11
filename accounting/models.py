from sqlalchemy import Column, Integer, String

from gateway.database import Base


class Accounting(Base):
    __tablename__ = "accounting"

    id = Column(Integer, primary_key=True, index=True)
    account_type = Column(String, unique=True, index=True)
    account_holder_name = Column(String, index=True)
    account_holder_age = Column(Integer, index=True)
