from abc import ABCMeta, abstractmethod

from general.exceptions import DataNotFoundException


class User:
    def __init__(self, username, password, first_name, last_name):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name



class UserDataSource(metaclass=ABCMeta):
    @abstractmethod
    def create_user(self, username, password):
        pass

    @abstractmethod
    def username_exist(self, username):
        pass

    @abstractmethod
    def update_profile(self, user, first_name, last_name):
        pass

    @abstractmethod
    def get_user(self, username):
        pass

    @abstractmethod
    def get_users(self):
        pass


class UserRamDataSource(UserDataSource):
    def __init__(self):
        self.users = []

    def create_user(self, username, password):
        self.users.append(User(username, password, '', ''))

    def username_exist(self, username):
        for user in self.users:
            if user.username == username:
                return True

        return False

    def update_profile(self, user, first_name, last_name):
        user.first_name = first_name
        user.last_name = last_name

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user

        raise DataNotFoundException()

    def get_users(self):
        return self.users
