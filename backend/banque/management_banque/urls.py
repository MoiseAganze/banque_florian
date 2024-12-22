from .views import BankAccountView
from django.urls import path
urlpatterns = [
    path("create_bank_account/", BankAccountView.as_view(), name="create_bank_account"),
]
