from typing import Optional, List
from database import PgDriver
from model.model_product import PydanticProduct


class ManagerProduct(object):

    @staticmethod
    async def get_product() -> Optional[List[PydanticProduct]]:
        with PgDriver() as curr:
            curr.execute(
                """
                SELECT * FROM products
                """
            )
            items = curr.fetchall()

        return [PydanticProduct(**item) for item in items] if items else None
