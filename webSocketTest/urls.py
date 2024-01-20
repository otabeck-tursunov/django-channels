from django.contrib import admin
from django.urls import path

from navbat.views import PersonPostAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person_create/', PersonPostAPI.as_view())
]
