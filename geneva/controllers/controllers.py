from geneva.models import Persona

class PersonaController:
    @staticmethod
    def crear_persona(persona_dto):
        persona = Persona(nombre=persona_dto.nombre, edad=persona_dto.edad)
        persona.save()

    @staticmethod
    def obtener_personas():
        return Persona.objects.all()
