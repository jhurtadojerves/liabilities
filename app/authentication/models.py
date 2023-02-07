from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from app.core.models import TimeStamped


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def save(self, *args, **kwargs):
        created = self.id is None
        super().save(*args, **kwargs)

        if created:
            Profile.objects.create(user=self)

    def __str__(self):
        return self.username

    def get_profile(self):
        if hasattr(self, "profile"):
            return self.profile

        return False


class Profile(TimeStamped):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = "users profile"

    def __str__(self):
        return str(self.user)
