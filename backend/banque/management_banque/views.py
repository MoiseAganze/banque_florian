from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.views import APIView
from .models import BankAccount
from .serializers import BankAccountSerializer
from rest_framework import generics
from rest_framework.fields import CurrentUserDefault
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
class ViewBankAccount(generics.ListAPIView) :
    """
    cette vue permetra à user de verifier son compte banciare apres avoir remplit ces conditions
    1 etre connecté
    2 entrer un bon code pin 
    """
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated]
    def get(self,request, *args, **kwargs) :
        pin_sended = request.query_params.get("pin")
        if not pin_sended:
            return Response({"detail":"le code pin est requis pour verifier le compte "}, status=status.HTTP_400_BAD_REQUEST)
        try :
            account = BankAccount.objects.get(user=request.user)
        except BankAccount.DoesNotExist :
            return Response({"detail":"vous n'avez pas de compte de bancaire !"})
        if pin_sended != account.pin_code:
            return Response({"detail":"le code pin est incorrect !"})
        return Response(self.get_serializer(account).data)
class VerifyAccountNumber(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        account_number = request.data.get("account_number")
        if not account_number:
            return Response({"detail":"le numero est requis pour cette opération !"})
        try :
            account = BankAccount.objects.get(account_number=account_number)
            if account_number == account.account_number:
                return Response({"deatil":"numero de compte valide !"}, status=status.HTTP_200_OK)
        except BankAccount.DoesNotExist:
            return Response({"deatil":"le compte pour ce numero n'a pas été trouvé !"}, status=status.HTTP_400_BAD_REQUEST)
class ResetCodePin(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,*args, **kwargs):
        account_number = request.data.get("account_number")
        pin = request.data.get("new_pin")
        try:
            account = BankAccount.objects.get(account_number=account_number, user=request.user)
            account.pin_code = pin
            account.save()
            return Response({"detail":"le code pin a été changé avec succes !"}, status=status.HTTP_200_OK)
        except BankAccount.DoesNotExist :
            return Response({"detail":"Compte bancaire non trouvé !"}, status=status.HTTP_400_BAD_REQUEST)
    