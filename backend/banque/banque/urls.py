
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("User.urls")),
    path("FS-Bank/", include("management_banque.urls")),
    path('admin/', admin.site.urls),
]
