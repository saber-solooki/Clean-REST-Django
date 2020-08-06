from main.domain.sigup_repo import SingUpRepo


class SignupRepoImpl(SingUpRepo):
    def create_user(self, username, password):
        self.data_source.create_user(username, password)

    def username_exist(self, username):
        return self.data_source.username_exist(username)
