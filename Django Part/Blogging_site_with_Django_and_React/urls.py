
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('auth/', obtain_auth_token),
]


## Blogging_site_with_Django_and_React

# py manage.py makemigrations
# py manage.py migrate
# py manage.py runserver