from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import BankAccountSerializer
class BankAccountView(APIView):
    permission_classes = [IsAuthenticated]  
    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data.copy()  
        data['user'] = user.id 
        serializer = BankAccountSerializer(data=data,context={'request': request})
        """
        le context je peux pas l'oublier car ça me permet le user au context  dans le serialiser user=self.context["request"].user
        """
        if serializer.is_valid(): 
            bank_account = serializer.save()  
            print(f"Numéro de compte généré : {bank_account.account_number}")
            return Response({
                "message": "Le numéro de compte a été généré, gardez bien cela",
                "account_number": bank_account.account_number,
            }, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

