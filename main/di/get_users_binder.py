from main.data.get_users import GetUsersRepoImpl
from main.domain.get_users_repo import GetUsersRepo
from main.domain.use_cases.get_users import GetUsersUseCase


def provide_use_case():
    return GetUsersUseCase()


def provide_repo():
    return GetUsersRepoImpl()


def get_users_binder(binder):
    binder.bind_to_provider(GetUsersUseCase, provide_use_case)
    binder.bind_to_provider(GetUsersRepo, provide_repo)
