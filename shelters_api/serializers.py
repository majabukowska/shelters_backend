from rest_framework import serializers
from .models import Pet, Shelter, User

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class ShelterSerializer(serializers.ModelSerializer):
    pets = PetSerializer(many=True, read_only=True)

    class Meta:
        model = Shelter
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    liked_pets = PetSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'liked_pets']
