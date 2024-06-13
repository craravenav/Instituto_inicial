from django.shortcuts import render
from .models import Alumno,Genero

# Create your views here.
class persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()


def index(request):
    
    alumnos = Alumno.objects.all()
    context = {"alumnos":alumnos}

    #hijo=persona("Juan Perez", "7")
    #lista=["Lazaña", "Charquican", "Porotos granado"]
    #context={"hijo":hijo, "nombre":"Claudia Andrea", "comidas":lista}

    return render(request, 'alumnos/index.html', context)