from django.urls import path

from main.views import SignUpView, UpdateProfile, GetUserList, users_page

app_name = 'main'


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('update/', UpdateProfile.as_view(), name='update'),
    path('list/users/', GetUserList.as_view(), name='users'),
    path('users-page/', users_page, name='users-page'),
]