from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PetViewSet, ShelterViewSet, UserViewSet

router = DefaultRouter()
router.register(r'pets', PetViewSet)
router.register(r'shelters', ShelterViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
