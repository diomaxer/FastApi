from typing import Optional, List

from fastapi import APIRouter
from starlette import status

from model.model_auth import PydanticCreateUser
from service.service_auth import SrviceAuth

router = APIRouter()


@router.post(
    path="/register/",
    status_code=status.HTTP_201_CREATED,
    description="Register",
    response_model=PydanticCreateUser,
)
async def register(user: PydanticCreateUser):
    return await SrviceAuth.register(user=user)
