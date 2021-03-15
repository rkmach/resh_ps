from django.urls import path, include
from .views import RegisterView, HomePageView, MyUserLoginView, LogoutPageView, ChangePasswordView, DeleteAccountView, ChangeUserInfoView
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'pages'

urlpatterns = format_suffix_patterns([
    path('registration/', RegisterView.as_view(), name='register'),
    path("home/", HomePageView.as_view(), name="home"),
    path('login/', MyUserLoginView.as_view(), name='login'),
    path("logout/", LogoutPageView.as_view(), name="logout"),
    path("change_password/", ChangePasswordView.as_view(), name="change_password"),
    path("delete_account/", DeleteAccountView.as_view(), name="delete"),
    path("change_info/", ChangeUserInfoView.as_view(), name="change_info"),
])