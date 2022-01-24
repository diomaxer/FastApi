from typing import Optional, List

from fastapi import APIRouter
from starlette import status

from model.model_product import PydanticProduct
from service.service_product import ServiceProduct

router = APIRouter()


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    description="Товары",
    response_model=Optional[List[PydanticProduct]],
)
async def get_products():
    return await ServiceProduct.get_product()
