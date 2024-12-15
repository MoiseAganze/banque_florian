

from rest_framework import serializers
from .models import InscriptionModel

class InscriptionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InscriptionModel
        fields = ['email', 'nom_complet', 'telephone', 'adresse', 'data_inscription']
