from rest_framework import serializers
from authentication.models import CustomUser
from django.contrib.auth.hashers import make_password


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ["last_login", "groups"]
        # fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop("password")
        hashed_password = make_password(password)
        validated_data["password"] = hashed_password
        return super().create(validated_data)

    def update(self, instance, validated_data):
        password = validated_data.get("password")
        if password:
            hashed_password = make_password(password)
            validated_data["password"] = hashed_password
        return super().update(instance, validated_data)


class CustomUserforOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "first_name", "last_name")
