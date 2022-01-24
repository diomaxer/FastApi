from database import PgDriver
from model.model_auth import PydanticCreateUser


class ManagerAuth(object):
    @staticmethod
    async def register(user: PydanticCreateUser):

        with PgDriver() as curr:
            curr.execute(
                """
                INSERT INTO users (username, email, password) VALUES (%s, %s, %s)
                """, (user.username, user.email, user.password)
            )