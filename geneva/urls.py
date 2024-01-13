# personas/urls.py
from django.urls import path
from geneva.views import views

urlpatterns = [
    path('listar/', views.listar_personas, name='listar_personas'),
    path('crear/', views.crear_persona, name='crear_persona'),
    # Puedes agregar más URL patterns según las operaciones que desees realizar
]
