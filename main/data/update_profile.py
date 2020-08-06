from main.domain.update_profile_repo import UpdateProfileRepo


class UpdateProfileRepoImpl(UpdateProfileRepo):
    def get_user(self, username):
        return self.data_source.get_user(username)

    def update_entity(self, user, first_name, last_name):
        self.data_source.update_profile(user, first_name, last_name)
