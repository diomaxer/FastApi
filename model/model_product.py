from pydantic import BaseModel, validator


class PydanticProduct(BaseModel):
    id: int
    name: str
    price: int
    customer_id: int
