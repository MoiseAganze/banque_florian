# views.py

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from .models import GestionUtilisateur, InscriptionModel
from .serializer import InscriptionModelSerializer
import re

class INcs(generics.CreateAPIView) :
    queryset = InscriptionModel.objects.all()
    serializer_class = InscriptionModelSerializer