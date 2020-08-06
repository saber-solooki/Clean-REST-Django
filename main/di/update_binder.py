from main.data.update_profile import UpdateProfileRepoImpl
from main.domain.update_profile_repo import UpdateProfileRepo
from main.domain.use_cases.update_profile import UpdateProfileUseCase


def provide_use_case():
    return UpdateProfileUseCase()


def provide_repo():
    return UpdateProfileRepoImpl()


def update_binder(binder):
    binder.bind_to_provider(UpdateProfileUseCase, provide_use_case)
    binder.bind_to_provider(UpdateProfileRepo, provide_repo)
