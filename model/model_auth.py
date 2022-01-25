from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, root_validator, validator
from starlette import status


class PydanticUser(BaseModel):
    id: int
    username: str
    email: Optional[str]
    password: str


class PydanticCreateUser(BaseModel):
    username: str
    email: Optional[str]
    password: str
    password2: str

    @validator('password')
    def password_check(cls, v):
        if v is None or len(v) < 6:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Password less then 6 digits")
        low_password = v.lower()
        for char in low_password:
            if char in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Password contains russians letters")
        return v

    @root_validator(pre=True)
    def passwords_matching(cls, values):
        pw1, pw2 = values.get('password'), values.get('password2')
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Passwords didn't match")
        return values
