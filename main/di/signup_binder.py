from main.data.signup_repo import SignupRepoImpl
from main.domain.sigup_repo import SingUpRepo
from main.domain.use_cases.sign_up import SignUpUseCase


def provide_use_case():
    return SignUpUseCase()


def provide_repo():
    return SignupRepoImpl()


def signup_binder(binder):
    binder.bind_to_provider(SignUpUseCase, provide_use_case)
    binder.bind_to_provider(SingUpRepo, provide_repo)
