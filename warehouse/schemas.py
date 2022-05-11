from pydantic import BaseModel


class WareHouse(BaseModel):
    id: int
    name: str
    address: str
    city: str
    country: str

    class Config:
        orm_mode = True
