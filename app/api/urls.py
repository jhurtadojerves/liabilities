from rest_framework.routers import DefaultRouter

from app.authentication.viewsets import UserViewSet

router = DefaultRouter(trailing_slash=True)

router.register("users", UserViewSet, basename="users")


urlpatterns = router.urls
