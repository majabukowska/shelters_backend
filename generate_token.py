import os
import django

# Ustawienie zmiennej środowiskowej dla ustawień Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shelters_backend.settings')

# Inicjalizacja Django
django.setup()

from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

def create_static_token():
    user = User.objects.get(username='superuser')  # Zmień na nazwę swojego superusera
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)
    print(f'Static Token for superuser: {token}')

if __name__ == '__main__':
    create_static_token()
