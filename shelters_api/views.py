from rest_framework import viewsets, permissions
from .models import Pet, Shelter, User
from .serializers import PetSerializer, ShelterSerializer, UserSerializer
from rest_framework.parsers import MultiPartParser, FormParser



class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    parser_classes = (MultiPartParser, FormParser)

class ShelterViewSet(viewsets.ModelViewSet):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer
    parser_classes = (MultiPartParser, FormParser)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
