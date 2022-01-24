from manager.manager_product import ManagerProduct


class ServiceProduct(object):

    @staticmethod
    async def get_product():
        return await ManagerProduct.get_product()
