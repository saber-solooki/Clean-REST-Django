from core_architecture.entity import PagedDataEntity
from core_architecture.pagination import PaginatorQueryWrapper
from main.domain.entity.user import User
from main.domain.get_users_repo import GetUsersRepo


class GetUsersRepoImpl(GetUsersRepo):
    def get_user_list(self, page) -> PagedDataEntity[User]:
        users = self.data_source.get_users()
        query_wrapper = PaginatorQueryWrapper(User)
        return query_wrapper.get_paginated_data(users, page)
