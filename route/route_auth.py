from typing import Optional, List

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from model.model_auth import PydanticCreateUser
from service.service_auth import ServiceAuth

router = APIRouter()


@router.post(
    path="/register/",
    status_code=status.HTTP_201_CREATED,
    description="Register",
    response_model=PydanticCreateUser,
    responses={
        422: {
            "content": {"application/json": {"example": {"detail": "Passwords didn't match"}}},
        }
    })
async def register(user: PydanticCreateUser):
    return await ServiceAuth.register(user=user)


@router.post(
    path="/login/",
    status_code=status.HTTP_201_CREATED,
    description="Login",
    # response_model=PydanticCreateUser,
    responses={
        422: {
            "content": {"application/json": {"example": {"detail": "Login or password didn't match"}}},
        }
    })
async def register(form_data: OAuth2PasswordRequestForm = Depends()):
    return await ServiceAuth.login(form_data=form_data)
