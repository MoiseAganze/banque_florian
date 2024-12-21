from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import BankAccountSerializer

class BankAccountView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BankAccountSerializer(data=request.data)
        if serializer.is_valid(): 
            bank_account = serializer.save()  
            print(f"Numéro de compte généré : {bank_account.account_number}")
            return Response({
                "message": "Le numéro de compte a été généré, gardez bien cela",
                "account_number": bank_account.account_number,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
