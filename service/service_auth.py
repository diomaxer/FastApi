from manager.manager_auth import ManagerAuth
from model.model_auth import PydanticCreateUser


class SrviceAuth(object):

    @staticmethod
    async def register(user: PydanticCreateUser):
        await ManagerAuth.register(user=user)
