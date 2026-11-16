
from django.http import HttpResponse

def home(request):
    return HttpResponse(
        "<h1>Creación de mi primera aplicacion: aplicacionInicial</h1>"
        "<p>Entorno instalado y proyecto inicial correcto..</p>"
    )
