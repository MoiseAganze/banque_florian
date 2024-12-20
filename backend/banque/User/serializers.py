from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
modelUser = get_user_model()
class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email","username","first_name", "last_name","password"]
        extra_Kwargs = {
            "password" : {"wrile_only": True}
        }
    def create(self,validated_data) :
        try : 
            user = modelUser.objects.create_user(
                email=validated_data["email"],
                username=validated_data["username"],
                first_name = validated_data["first_name"],
                last_name = validated_data['last_name'],
                password=validated_data["password"]
            )
            return user
        except KeyError as e:
            raise serializers.ValidationError(f"le champ {e} est oblogatoire")
class Userlogin(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    def validate(self, data):
        email = data["email"]
        password = data["password"]
        user = authenticate(email=email,password=password)
        if not user:
            raise serializers.ValidationError("l'email ou mot de passe inscorrect !")
        return user


