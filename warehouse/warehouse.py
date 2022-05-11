from sqlalchemy.orm import Session

from . import models


def get_warehouse_data(db: Session, skip: int = 0, limit: int = 100):
    __doc__ = "this method is used to return the all data of warehouse"
    warehouse_date = db.query(models.WareHouse).offset(skip).limit(limit).all()
    return warehouse_date if warehouse_date else []

