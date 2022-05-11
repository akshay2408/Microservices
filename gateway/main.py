from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from accounting import accounting as accounting_data, models as accounting_model
from warehouse import warehouse as warehouse_data, models as warehouse_model
from sales import sales as sales_data, models as sales_model
from gateway.database import SessionLocal, engine

accounting_model.Base.metadata.create_all(bind=engine)
warehouse_model.Base.metadata.create_all(bind=engine)
sales_model.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/get_all_microservice_data/")
def all_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    accounting = accounting_data.get_accounting_data(db, skip=skip, limit=limit)
    warehouse = warehouse_data.get_warehouse_data(db, skip=skip, limit=limit)
    sales = sales_data.get_sales_data(db, skip=skip, limit=limit)
    return {'accounting': accounting, 'warehouse': warehouse, 'sales': sales}