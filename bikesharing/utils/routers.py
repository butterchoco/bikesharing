from rest_framework import routers
from .views import UserViewSet

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
