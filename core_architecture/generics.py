from core_architecture.mixin import RetrieveDataMixin, CreateDataMixin, DestroyDataMixin, UpdateDataMixin
from core_architecture.view import CleanAPIView


class CleanGenericAPIView(CleanAPIView):
    serializer_class = None
    pass


class CARetrieveAPIView(RetrieveDataMixin, CleanGenericAPIView):
    def get(self, request, *args, **kwargs):
        self.check_request_data(request)
        return self.retrieve(request, *args, **kwargs)


class CACreateAPIView(CreateDataMixin, CleanGenericAPIView):
    def post(self, request, *args, **kwargs):
        self.check_request_data(request)
        return self.create(request, *args, **kwargs)


class DestroyAPIView(DestroyDataMixin, CleanGenericAPIView):
    def delete(self, request, *args, **kwargs):
        self.check_request_data(request)
        return self.destroy(request, *args, **kwargs)


class UpdateAPIView(UpdateDataMixin, CleanGenericAPIView):
    def put(self, request, *args, **kwargs):
        self.check_request_data(request)
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        self.check_request_data(request)
        return self.partial_update(request, *args, **kwargs)