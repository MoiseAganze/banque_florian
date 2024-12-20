from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers import UserSerialiser,Userlogin
permission_classes = [IsAuthenticated]
class UserTokenObtainPairView(TokenObtainPairView):
    pass
class UserTokenRefresh(TokenRefreshView):
    pass
class CreateUserview(generics.CreateAPIView) :
    serializer_class = UserSerialiser
@api_view(["POST"])
def login_user(request, *args, **kwargs) :
    if request.method == "POST" :
        print(request.data)
        serialiser = Userlogin(data=request.data)
        if serialiser.is_valid(raise_exception=True):
            user = serialiser.validated_data
            refresh_token = RefreshToken.for_user(user) # token pour rafraichier
            access_token = refresh_token.access_token # token pour l'acces
            return Response({
                "token_refresh" : str(refresh_token),
                "acces_token":str(access_token)
            }, status=status.HTTP_200_OK)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
            
