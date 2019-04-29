from rest_framework import routers
from .views import UserViewSet, PersonViewSet

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'person', PersonViewSet)