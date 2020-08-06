from collections import OrderedDict
from typing import Generic, Type

from django.conf import settings
from rest_framework.response import Response
from rest_framework.utils.urls import replace_query_param, remove_query_param

from core_architecture import T
from core_architecture.entity import PagedDataEntity


class PaginatorResponseWrapper:
    page_query_param = 'page'

    def __init__(self, request, paged_data):
        self.request = request
        self.paged_data = paged_data

    def get_paginated_response(self, data_result):
        return Response(OrderedDict([
            ('count', self.paged_data.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data_result)
        ]))

    def get_next_link(self):
        if not self.paged_data.has_next:
            return None
        url = self.request.build_absolute_uri()
        page_number = self.paged_data.next_page_number
        return replace_query_param(url, self.page_query_param, page_number)

    def get_previous_link(self):
        if not self.paged_data.has_previous:
            return None
        url = self.request.build_absolute_uri()
        page_number = self.paged_data.previous_page_number
        if page_number == 1:
            return remove_query_param(url, self.page_query_param)
        return replace_query_param(url, self.page_query_param, page_number)


class PaginatorQueryWrapper(Generic[T]):
    def __init__(self, class_entity: Type[T]):
        self.class_entity = class_entity

    def get_paginated_data(self, query_set, page) -> PagedDataEntity[T]:
        from django.core.paginator import Paginator

        paginator = Paginator(query_set, settings.PAGE_SIZE)

        page = paginator.get_page(page)

        return PagedDataEntity(count=page.paginator.count, has_next=page.has_next(),
                               next_page_number=page.next_page_number() if page.has_next() else None,
                               has_previous=page.has_previous(),
                               previous_page_number=page.previous_page_number() if page.has_previous() else None,
                               number=page.number, num_pages=page.paginator.num_pages,
                               results=self._get_data_result(page))

    def _get_data_result(self, page):
        result = []
        for entity in page:
            object_entity = self.class_entity()
            for item in object_entity.__dict__.keys():
                setattr(object_entity, item, getattr(entity, item))
            result.append(object_entity)

        return result
