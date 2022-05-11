from pydantic import BaseModel


class Accounting(BaseModel):
    id: int
    account_type: str
    account_holder_name: str
    account_holder_age: int

    class Config:
        orm_mode = True
