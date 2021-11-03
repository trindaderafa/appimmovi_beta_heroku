from django.urls import include, path
from .views import home, lista_pessoas


urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas')
]