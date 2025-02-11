from django.shortcuts import render

# Create your views here.
def lista_recetas(request):
    return render(request, 'recetas/lista_recetas.html', {})
