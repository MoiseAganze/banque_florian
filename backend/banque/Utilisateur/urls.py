

# urls.py

from django.urls import path
from .views import  INcs

urlpatterns = [
    path('inscription/', INcs.as_view(), name='register_user'),
   ]
