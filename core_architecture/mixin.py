from django.utils.http import urlencode
from rest_framework import status
from rest_framework.response import Response


class RetrieveDataMixin:
    def retrieve(self, request, *args, **kwargs):
        data = self.get_data_query(request, *args, **kwargs)
        if self.serializer_class is None:
            return Response(data)
        else:
            return Response(self.serializer_class(data, many=self.is_many).data)


class CreateDataMixin:
    def create(self, request, *args, **kwargs):
        data = self.perform_create_data(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED, data=data)


class DestroyDataMixin:
    def destroy(self, request, *args, **kwargs):
        self.perform_destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateDataMixin(object):
    def update(self, request, *args, **kwargs):
        self.perform_update(request, *args, **kwargs)
        return Response(status=status.HTTP_202_ACCEPTED)

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class QueryStringMixin:
   def get_query_string(self, new_params=None, remove=None):
       if new_params is None:
           new_params = {}
       if remove is None:
           remove = []
       p = self.params.copy()
       for r in remove:
           for k in list(p):
               if k.startswith(r):
                   del p[k]
       for k, v in new_params.items():
           if v is None:
               if k in p:
                   del p[k]
           else:
               p[k] = v
       return '?%s' % urlencode(sorted(p.items()))