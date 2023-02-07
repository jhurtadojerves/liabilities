from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission
from rest_framework.viewsets import GenericViewSet, mixins

from app.authentication.serializers import UserSerializer

User = get_user_model()


class UserViewSet(
    GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    lookup_field = "username"
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [BasePermission]
