from django.contrib import admin
from .models import BankAccount
class AdminBankAccount(admin.ModelAdmin):
    list_display = [
        "user","account_number","type_compte","account_solde","account_status","first_name",
        "last_name","email","phone_number","civility","agency","birth_day","nationality",
        "zip_code","pin_code"
    ]
admin.site.register(BankAccount, AdminBankAccount)