import inject

from general.exceptions import BusinessException
from general.validator import PasswordValidator
from main.domain.sigup_repo import SingUpRepo


class SignUpUseCase:
    @inject.autoparams()
    def __init__(self, repo: SingUpRepo, password_validator: PasswordValidator):
        self.repo = repo
        self.password_validator = password_validator

    def create_user(self, username, password):
        if self.repo.username_exist(username):
            raise BusinessException(code=BusinessException.USERNAME_EXIST)

        self.password_validator.validate_password(password)

        self.repo.create_user(username, password)
