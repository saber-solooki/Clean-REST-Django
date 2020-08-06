from abc import ABCMeta, abstractmethod

from django.contrib.auth.password_validation import validate_password, get_password_validators
from django.core.exceptions import ValidationError

from example import settings
from general.exceptions import BusinessException


class PasswordValidator(metaclass=ABCMeta):
   @abstractmethod
   def validate_password(self, value):
       pass


class DjangoPasswordValidator(PasswordValidator):
   def validate_password(self, value):
       if len(get_password_validators(settings.AUTH_PASSWORD_VALIDATORS)) > 0:
           try:
               validate_password(value)
               return value
           except ValidationError as e:
               raise BusinessException(code=BusinessException.PASSWORD_VALIDATION_ERROR, message="\n".join(e.messages))
       else:
           return value

