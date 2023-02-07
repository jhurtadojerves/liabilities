from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import pgettext_lazy
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from app.authentication.validators import validate_password_strength

User = get_user_model()


class UserSerializer(ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password1 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password, validate_password_strength],
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )
    url = serializers.HyperlinkedIdentityField(
        view_name="api:users-detail", lookup_field="username"
    )

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "username", "url"]

    def validate_password2(self, password2):
        if password2 != self.initial_data.get("password1"):
            raise serializers.ValidationError(
                pgettext_lazy("User registration", "Passwords are not the same.")
            )

        return password2

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get("password"))
        user.save(update_fields=["password"])

        return user
