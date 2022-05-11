from sqlalchemy.orm import Session

from .import models


def get_accounting_data(db: Session, skip: int = 0, limit: int = 100):
    __doc__ = "this method is used to return the all data of accounting"
    accounting_data = db.query(models.Accounting).offset(skip).limit(limit).all()
    return accounting_data if accounting_data else []

