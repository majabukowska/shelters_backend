import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shelters_backend.settings')
django.setup()

from shelters_api.models import User
from rest_framework.authtoken.models import Token

def create_superuser_and_token():
    username = 'admin'
    email = 'admin@example.com'
    password = 'adminpassword'

    if not User.objects.filter(username=username).exists():
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print("Superuser created.")
    else:
        user = User.objects.get(username=username)
        print("Superuser already exists.")

    # Pobierz lub utwórz token dla użytkownika
    token, created = Token.objects.get_or_create(user=user)
    print(f'Static Token for superuser: {token.key}')

if __name__ == '__main__':
    create_superuser_and_token()
