from typing import Optional
from pydantic import BaseModel, root_validator


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

    @root_validator(pre=True)
    def password_check(cls, values):
        pw1, pw2 = values.get('password'), values.get('password2')
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError("Passwords don't match")
        if pw1 is not None and len(pw1) < 6:
            raise ValueError("Password less then 6 digits")
        print('Done')
        return values
