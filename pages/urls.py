from django.urls import path, include
from users.models import MyUser
from rest_framework import routers, serializers, viewsets
from .views import RegisterView, HomePageView, MyUserLoginView, LogoutPageView, ChangePasswordView, DeleteAccountView, ChangeUserInfoView
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.views import LoginView

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'login', MyUserViewSet, basename='login')

app_name = 'pages'

urlpatterns = format_suffix_patterns([
    path('registration/', RegisterView.as_view(), name='register'),
    path("home/", HomePageView.as_view(), name="home"),
    # path("login/", MyUserLoginView.as_view(), name="login"),
    path('login/', MyUserLoginView.as_view(), name='login'),
    path("logout/", LogoutPageView.as_view(), name="logout"),
    path("change_password/", ChangePasswordView.as_view(), name="change_password"),
    path("delete_account/", DeleteAccountView.as_view(), name="delete"),
    path("change_info/", ChangeUserInfoView.as_view(), name="change_info"),
    # path('registration-success/', MyUserRegistrationView.as_view(), name="user-create"),
    # path('login/', LoginView.as_view(), name='login'),
    # path('users/<int:pk>/', user_detail, name='user-detail'),
])