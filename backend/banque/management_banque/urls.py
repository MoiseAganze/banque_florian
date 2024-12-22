from .views import BankAccountView,user_info
from django.urls import path
urlpatterns = [
    path("create_bank_account/", BankAccountView.as_view(), name="create_bank_account"),
     path('user_info/', user_info, name='user_info'),
]
