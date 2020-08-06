from abc import ABCMeta, abstractmethod

import inject

from main.data.data_source import UserDataSource


class SingUpRepo(metaclass=ABCMeta):
    @inject.autoparams()
    def __init__(self, data_source: UserDataSource):
        self.data_source = data_source

    @abstractmethod
    def create_user(self, username, password):
        pass

    @abstractmethod
    def username_exist(self, username):
        pass
