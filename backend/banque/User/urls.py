
from django.urls import path
from .views import UserTokenObtainPairView,UserTokenRefresh,CreateUserView, login_user
urlpatterns = [
    path("api/token/", UserTokenObtainPairView.as_view(), name="userapitoken"),
    path("api/token/refresh/", UserTokenRefresh.as_view(), name="api_refresh_token"),
    path("inscription_user/", CreateUserView.as_view(), name="CreateUserview"),
    path("login_user/", login_user, name="login_user"),
]
