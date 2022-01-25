from typing import Optional

from database import PgDriver
from model.model_auth import PydanticCreateUser, PydanticUser


class ManagerAuth(object):

    @staticmethod
    async def check_username(username: str) -> Optional[PydanticUser]:
        with PgDriver() as curr:
            curr.execute(
                """
                SELECT * FROM users WHERE username = %s
                """, (username, )
            )
            item = curr.fetchone()

        return PydanticUser(**dict(item)) if item else None

    @staticmethod
    async def register(user: PydanticCreateUser):

        with PgDriver() as curr:
            curr.execute(
                """
                INSERT INTO users (username, email, password) VALUES (%s, %s, %s)
                """, (user.username, user.email, user.password)
            )