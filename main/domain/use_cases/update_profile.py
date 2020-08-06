import inject

from main.domain.update_profile_repo import UpdateProfileRepo


class UpdateProfileUseCase:
    @inject.autoparams()
    def __init__(self, repo: UpdateProfileRepo):
        self.repo = repo

    def update_user_profile(self, username, first_name, last_name):
        user = self.repo.get_user(username)
        self.repo.update_entity(user, first_name, last_name)
