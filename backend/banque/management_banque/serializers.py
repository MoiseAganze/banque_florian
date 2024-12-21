from rest_framework import serializers
from random import randint
from .models import BankAccount

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = [
        "user","type_compte","account_solde","account_status","first_name",
        "last_name","email","phone_number","civility","agency","birth_day","nationality",
        "zip_code","pin_code"
    ]

    def generate_account_number(self):
        """Génère un numéro de compte unique"""
        prefix_number = "155"
        aleatoire_number = "".join(str(randint(0, 9)) for _ in range(10))
        return prefix_number + aleatoire_number

    def create(self, validated_data):
        """Crée un nouveau compte avec un numéro généré"""
        # Crée un nouvel objet BankAccount en utilisant les données validées et un numéro de compte généré
        bank_account = BankAccount.objects.create(
            user=validated_data["user"],
            account_number=self.generate_account_number(),  # Utilise la méthode de génération de numéro de compte
            type_compte=validated_data["type_compte"],
            account_solde=validated_data["account_solde"],
            account_status=validated_data["account_status"],  # Corrigé pour ne pas avoir de liste
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            phone_number=validated_data["phone_number"],  # Corrigé pour ne pas avoir de liste
            civility=validated_data["civility"],
            agency=validated_data["agency"],
            birth_day=validated_data["birth_day"],
            nationality=validated_data["nationality"],
            zip_code=validated_data["zip_code"],
            pin_code=validated_data["pin_code"]
        )
        return bank_account
