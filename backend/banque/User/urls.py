
from django.urls import path
from .views import UserTokenObtainPairView,UserTokenRefresh,CreateUserview, login_user
urlpatterns = [
    path("api/token/", UserTokenObtainPairView.as_view(), name="userapitoken"),
    path("api/token/refresh/", UserTokenRefresh.as_view(), name="api_refresh_token"),
    path("CreateUserview/", CreateUserview.as_view(), name="CreateUserview"),
    path("login_user/", login_user, name="login_user"),
]
