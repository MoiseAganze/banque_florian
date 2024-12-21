
from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model,authenticate
UserModel = get_user_model()
class UserSerialiser(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ["first_name", "last_name","username","email", "password"]
        extra_kwargs = {
            "password" : {"write_only":True}
        }
    def create(self, validated_data) :
        try : 
            user = UserModel.objects.create_user(
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
            )
            return user
        except KeyError as e:
            raise serializers.ValidationError(f"le champ {e} est obligatoire")
class UserLoginSerialiser(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    def validate(self, data) :
        email = data["email"]
        password = data["password"]
        user = authenticate(
            email=email,password=password
        )
        if not  user:
            raise serializers.ValidationError("l'email ou mot de passe incorrect !")
        return user
        