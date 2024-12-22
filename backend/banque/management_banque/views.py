from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import BankAccountSerializer
from rest_framework.decorators import api_view, permission_classes

class BankAccountView(APIView):
    permission_classes = [IsAuthenticated]  # S'assurer que l'utilisateur est authentifié
    
    def post(self, request, *args, **kwargs):
        # Récupérer l'utilisateur authentifié
        user = request.user
        
        # Ajouter l'utilisateur aux données de la requête avant de sérialiser
        data = request.data.copy()  # Créer une copie des données pour éviter toute modification directe
        data['user'] = user.id  # Associer l'utilisateur connecté au compte bancaire

        # Passer les données modifiées au serializer
        serializer = BankAccountSerializer(data=data,context={'request': request})

        if serializer.is_valid(): 
            # Sauvegarder le compte bancaire
            bank_account = serializer.save()  
            print(f"Numéro de compte généré : {bank_account.account_number}")
            return Response({
                "message": "Le numéro de compte a été généré, gardez bien cela",
                "account_number": bank_account.account_number,
            }, status=status.HTTP_201_CREATED)
        
        # Retourner une réponse d'erreur si le serializer n'est pas valide
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    """
    Cette vue permet de récupérer les informations de l'utilisateur connecté.
    """
    user = request.user  # L'utilisateur connecté est accessible via request.user
    user_data = {
        'id': user.id,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        # Ajouter d'autres champs si nécessaire
    }
    return Response(user_data)
