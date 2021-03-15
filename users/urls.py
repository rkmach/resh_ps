from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GetAllUsernames
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"all_users", GetAllUsernames, basename='all_users')

app_name = "users"

urlpatterns = [
    path("", include(router.urls))
    # path('all_usernames/', GetAllUsernames.as_view()),
]