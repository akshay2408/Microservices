from pydantic import BaseModel


class Sales(BaseModel):
    name: str
    sales_type: str
    sales_type: str

    class Config:
        orm_mode = True
