from abc import ABCMeta, abstractmethod

import inject

from main.data.data_source import UserDataSource


class UpdateProfileRepo(metaclass=ABCMeta):
    @inject.autoparams()
    def __init__(self, data_source: UserDataSource):
        self.data_source = data_source

    @abstractmethod
    def get_user(self, username):
        pass

    @abstractmethod
    def update_entity(self, user, first_name, last_name):
        pass
