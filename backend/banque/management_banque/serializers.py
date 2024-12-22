from rest_framework import serializers
from random import randint
from .models import BankAccount
from rest_framework.fields import CurrentUserDefault
class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = [
            "type_compte", "account_solde", "account_status", "first_name",
            "last_name", "email", "phone_number", "civility", "agency",
            "birth_day", "nationality", "zip_code", "pin_code"
        ]
    def generate_account_number(self):
        """Génère un numéro de compte unique"""
        prefix_number = "155"
        aleatoire_number = "".join(str(randint(0, 9)) for _ in range(10))
        return prefix_number + aleatoire_number
    def create(self, validated_data):
        """Crée un nouveau compte avec un numéro de compte généré et associe l'utilisateur connecté"""        
        account_number = self.generate_account_number()
        bank_account = BankAccount.objects.create(
            user=self.context['request'].user,  
            account_number=account_number, 
            type_compte=validated_data["type_compte"],
            account_solde=validated_data["account_solde"],
            account_status=validated_data["account_status"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            phone_number=validated_data["phone_number"],
            civility=validated_data["civility"],
            agency=validated_data["agency"],
            birth_day=validated_data["birth_day"],
            nationality=validated_data["nationality"],
            zip_code=validated_data["zip_code"],
            pin_code=validated_data["pin_code"]
        )
        return bank_account
