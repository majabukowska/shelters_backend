from django.contrib import admin
from django.urls import path, include
from shelters_api import urls as shelters_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(shelters_api)),
]
