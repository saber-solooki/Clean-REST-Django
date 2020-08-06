from rest_framework import status
from rest_framework.response import Response

from general.exceptions import BusinessException, DataNotFoundException


def custom_exception_handler(exc, context):
    if isinstance(exc, BusinessException):
        if exc.code == BusinessException.PASSWORD_VALIDATION_ERROR:
            return Response({"error": exc.message}, status=status.HTTP_409_CONFLICT)
        elif exc.code == BusinessException.USERNAME_EXIST:
            return Response({"error": "username exist"}, status=status.HTTP_409_CONFLICT)
    elif isinstance(exc, DataNotFoundException):
        return Response({"error": "Entity not found"}, status=status.HTTP_404_NOT_FOUND)

    return None
