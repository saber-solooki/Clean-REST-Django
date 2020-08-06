import inject

from core_architecture.generics import CACreateAPIView, UpdateAPIView, CARetrieveAPIView
from core_architecture.view import CAListAPIView
from main.domain.use_cases.get_users import GetUsersUseCase
from main.domain.use_cases.sign_up import SignUpUseCase
from main.domain.use_cases.update_profile import UpdateProfileUseCase
from main.serializer import UserSerializer


class SignUpView(CACreateAPIView):
    @inject.autoparams()
    def __init__(self, use_case: SignUpUseCase, *args, **kwargs):
        super(SignUpView, self).__init__(*args, **kwargs)
        self.use_case = use_case
        self.username = None
        self.password = None

    def is_data_valid(self, request):
        self.username = request.data.get("username")
        self.password = request.data.get("password")
        if self.username is None or self.password is None:
            return False

        return True

    def perform_create_data(self, request):
        self.use_case.create_user(self.username, self.password)


class UpdateProfile(UpdateAPIView):
    @inject.autoparams()
    def __init__(self, use_case: UpdateProfileUseCase, *args, **kwargs):
        super(UpdateProfile, self).__init__(*args, **kwargs)
        self.use_case = use_case
        self.username = None
        self.first_name = None
        self.last_name = None

    def is_data_valid(self, request):
        self.username = request.data.get("username")
        self.first_name = request.data.get("first_name")
        self.last_name = request.data.get("last_name")
        if self.username is None:
            return False

        return True

    def perform_update(self, request):
        self.use_case.update_user_profile(self.username, self.first_name, self.last_name)


class GetProfile(CARetrieveAPIView):
    @inject.autoparams()
    def __init__(self, use_case: UpdateProfileUseCase, *args, **kwargs):
        super(GetProfile, self).__init__(*args, **kwargs)
        self.use_case = use_case
        self.username = None
        self.first_name = None
        self.last_name = None

    def is_data_valid(self, request):
        self.username = request.data.get("username")
        self.first_name = request.data.get("first_name")
        self.last_name = request.data.get("last_name")
        if self.username is None:
            return False

        return True


class GetUserList(CAListAPIView):
    serializer_class = UserSerializer

    @inject.autoparams()
    def __init__(self, use_case: GetUsersUseCase, *args, **kwargs):
        super(GetUserList, self).__init__(*args, **kwargs)
        self.use_case = use_case

    def get_list_query(self, request):
        page = request.query_params.get('page', 1)
        return self.use_case.get_users(page)
