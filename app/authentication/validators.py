from django.conf import settings
from django.utils.translation import pgettext_lazy
from rest_framework import serializers


def validate_password_strength(password):
    if password.upper() == password or password.lower() == password:
        raise serializers.ValidationError(
            {
                "password": pgettext_lazy(
                    "User registration",
                    "Password must contain at least 1 lower/upper case letter.",
                )
            }
        )

    if not any(char in password for char in settings.PASSWORD_REQUIRED_SYMBOLS):
        symbols = ", ".join(settings.PASSWORD_REQUIRED_SYMBOLS)
        message = (
            pgettext_lazy(
                "User registration",
                "Password must contain at least one of these special characters %(symbols)s",  # noqa: E501
            )
            % symbols
        )
        raise serializers.ValidationError(
            {"password": pgettext_lazy("User registration", message)}
        )

    return password
