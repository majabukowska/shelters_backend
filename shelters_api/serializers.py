from rest_framework import serializers
from .models import Pet, Shelter, User

class PetSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = Pet
        fields = '__all__'

class ShelterSerializer(serializers.ModelSerializer):
    pets = PetSerializer(many=True, read_only=True)
    image_url = serializers.ImageField(use_url=True, required=False, allow_null=True)  # Add this if Shelter has an ImageField

    class Meta:
        model = Shelter
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    liked_pets = PetSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'liked_pets']
