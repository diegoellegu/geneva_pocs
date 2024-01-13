from django.shortcuts import render

from geneva.controllers.controllers import PersonaController
from geneva.DTOs.dtos import PersonaDTO


def listar_personas(request):
    personas = PersonaController.obtener_personas()
    return render(request, 'listar_personas.html', {'personas': personas})

def crear_persona(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        edad = int(request.POST['edad'])
        persona_dto = PersonaDTO(nombre=nombre, edad=edad)
        PersonaController.crear_persona(persona_dto)
    return render(request, 'crear_persona.html')
