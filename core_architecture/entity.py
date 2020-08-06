from typing import List, Generic

import attr

from core_architecture import T


@attr.s(auto_attribs=True)
class PagedDataEntity(Generic[T]):
    count: int
    has_next: bool
    next_page_number: int
    has_previous: bool
    previous_page_number: int
    number: int
    num_pages: int
    results: List[T]
