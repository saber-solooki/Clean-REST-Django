from abc import ABC

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core_architecture.entity import PagedDataEntity
from core_architecture.exception import BadRequestException
from core_architecture.pagination import PaginatorResponseWrapper


class CleanAPIView(APIView):
    serializer_class = None
    is_many = False

    def check_request_data(self, request):
        if self.is_data_valid(request):
            self.check_general_business(request)
        else:
            raise BadRequestException

    def is_data_valid(self, request):
        return True

    def check_general_business(self, request):
        pass

    def get_data_query(self, request):
        pass

    def perform_create_data(self, request):
        pass

    def perform_destroy(self, request):
        pass

    def perform_update(self, request):
        pass

    def get_list_query(self, request) -> PagedDataEntity:
        pass


class CAListAPIView(CleanAPIView, ABC):
    def get(self, request, *args, **kwargs):
        self.check_request_data(request)
        paged_data = self.get_list_query(request)
        return self.get_paginated_response(paged_data, self.serializer_class(paged_data.results, many=True).data)

    def get_paginated_response(self, paged_data, data_result):
        paginator_wrapper = PaginatorResponseWrapper(self.request, paged_data)
        return paginator_wrapper.get_paginated_response(data_result)


