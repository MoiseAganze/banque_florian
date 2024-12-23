from .views import BankAccountView, ViewBankAccount,ResetCodePin,VerifyAccountNumber
from django.urls import path
urlpatterns = [
    path("create_bank_account/", BankAccountView.as_view(), name="create_bank_account"),
    path("ViewBankAccount/", ViewBankAccount.as_view(), name="ViewBankAccount"), 
    path("VerifyAccountNumber/", VerifyAccountNumber.as_view(), name="VerifyAccountNumber"), 
    path("ResetCodePin/", ResetCodePin.as_view(), name="ResetCodePin"), 
]
