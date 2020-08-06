import inject

from core_architecture.entity import PagedDataEntity
from main.domain.entity.user import User
from main.domain.get_users_repo import GetUsersRepo


class GetUsersUseCase:
    @inject.autoparams()
    def __init__(self, repo: GetUsersRepo):
        self.repo = repo

    def get_users(self, page) -> PagedDataEntity[User]:
        return self.repo.get_user_list(page)
