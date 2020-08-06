from rest_framework.exceptions import APIException


class BadRequestException(APIException):
    status_code = 400
    default_detail = 'Your request has not contain valid body or data'
    default_code = 'bad_request'
