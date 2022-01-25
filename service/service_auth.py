import os
import hashlib

from fastapi import HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from manager.manager_auth import ManagerAuth
from model.model_auth import PydanticCreateUser


class ServiceAuth(object):

    @staticmethod
    async def register(user: PydanticCreateUser) -> None:
        if await ManagerAuth.check_username(user.username):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Username is already taken")
        user.password = await ServiceAuth.hash_password(user.username)
        await ManagerAuth.register(user=user)

    @staticmethod
    async def login(form_data: OAuth2PasswordRequestForm) -> Response:
        user = ManagerAuth.check_username(form_data.username)

        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Password or username didn't match")
        if not await ServiceAuth._verify_password(plain_password=form_data.password, hashed_password=user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Password or username didn't match")

        response = Response()
        access_token = await ServiceAuth._create_access_token(email=user.email)
        response.set_cookie(
            key="Authorization",
            value=f"Bearer {access_token}",
            domain=ProjectConfig.URL_API_NO_SCHEMA
        )

        return response

    @staticmethod
    async def hash_password(password) -> bytes:
        salt = os.urandom(32)
        ket = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        storage = salt + ket
        return storage
