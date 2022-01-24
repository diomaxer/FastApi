from typing import Optional
from pydantic import BaseModel, root_validator


class PydanticProduct(BaseModel):
    id: Optional[int]
    name: str
    price: int
    customer_id: int
