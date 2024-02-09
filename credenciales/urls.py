from django.urls import path
from credenciales import views


urlpatterns = [
    path('', views.credenciales_view, name='credenciales'),
]

