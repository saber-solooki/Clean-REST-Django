from core_architecture.entity import PagedDataEntity
from core_architecture.mixin import QueryStringMixin


class HTMLPagingAdapter(QueryStringMixin):
    def __init__(self, query_params, data_entity: PagedDataEntity):
        self._page = HTMLPageAdapter(data_entity)
        self.data_list = data_entity.results

        self.params = dict(query_params)

    @property
    def page(self):
        return self._page


class HTMLPageAdapter:
    def __init__(self, data_entity: PagedDataEntity):
        self._paginator = HTMLPaginatorAdapter(data_entity.num_pages)
        self._number = data_entity.number

    @property
    def paginator(self):
        return self._paginator

    @property
    def number(self):
        return self._number


class HTMLPaginatorAdapter:
    def __init__(self, num_pages):
        self._num_pages = num_pages

    @property
    def num_pages(self):
        return self._num_pages
