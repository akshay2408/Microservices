from sqlalchemy.orm import Session

from . import models


def get_sales_data(db: Session, skip: int = 0, limit: int = 100):
    __doc__ = "this method is used to return the all data of sales"
    sales_data = db.query(models.Sales).offset(skip).limit(limit).all()
    return sales_data if sales_data else []

