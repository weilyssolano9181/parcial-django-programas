from django.shortcuts import render
from .forms import ProgramaForm


def crear_programa(request):
    mensaje = None
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "Programa registrado correctamente."
            form = ProgramaForm()
    else:
        form = ProgramaForm()

    return render(request, 'myapp/crear_programa.html', {'form': form, 'mensaje': mensaje})