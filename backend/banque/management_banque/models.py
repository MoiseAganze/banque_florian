from django.db import models
from django.contrib.auth.hashers import make_password
from phonenumbers import parse, is_valid_number
from django.core.exceptions import ValidationError
from datetime import date
from User.models import User
AFRICA_CENTRAL_COUNTRIES = [
    ('CD', 'République Démocratique du Congo (RDC)'),
    ('CG', 'République du Congo (Congo-Brazzaville)'),
    ('GA', 'Gabon'),
    ('CM', 'Cameroun'),
    ('TD', 'Tchad'),
]

def central_country(value):
    if value not in dict(AFRICA_CENTRAL_COUNTRIES).keys():
        raise ValidationError(f"Le pays {value} n'est pas pris en charge !")
    return value

class BankAccount(models.Model):
    TYPES_ACCOUNT = [
        ('actif', 'Actif'),
        ('inactif', 'Inactif'),
        ('bloqué', 'Bloqué'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=13)
    type_compte = models.CharField(max_length=30, choices=TYPES_ACCOUNT, default='actif')
    account_solde = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    account_status = models.CharField(max_length=20, default="actif")
    first_name = models.CharField(max_length=120) 
    last_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=120)
    civility = models.CharField(max_length=120)
    agency = models.CharField(max_length=120)
    birth_day = models.DateField()
    nationality = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=10)
    pin_code = models.CharField(max_length=4)

    def clean(self):
        # Logique de validation
        self.pin_code = make_password(self.pin_code)  
        if BankAccount.objects.filter(email=self.email).exists():
            raise ValidationError("Cet email existe déjà")
        phone_number = parse(self.phone_number)
        if not is_valid_number(phone_number):
            raise ValidationError("Le numéro de téléphone est invalide !")
        if BankAccount.objects.filter(phone_number=self.phone_number).exists():
            raise ValidationError(f"Un utilisateur avec le numéro de téléphone {self.phone_number} existe déjà !")
        today = date.today()
        if today.year - self.birth_day.year < 18:
            raise ValidationError("L'âge minimum requis est de 18 ans !")
        if len(self.pin_code) != 4:
            raise ValidationError("Le code PIN doit comporter exactement 4 chiffres !")
        if any(char.isalpha() for char in self.pin_code):
            raise ValidationError("Le code PIN ne peut pas contenir de lettres !")
        super().clean()
