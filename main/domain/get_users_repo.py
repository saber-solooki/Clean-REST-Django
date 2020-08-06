from abc import ABCMeta, abstractmethod

import inject

from core_architecture.entity import PagedDataEntity
from main.data.data_source import UserDataSource
from main.domain.entity.user import User


class GetUsersRepo(metaclass=ABCMeta):
    @inject.autoparams()
    def __init__(self, data_source: UserDataSource):
        self.data_source = data_source

    @abstractmethod
    def get_user_list(self, page) -> PagedDataEntity[User]:
        pass
