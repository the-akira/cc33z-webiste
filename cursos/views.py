from django.shortcuts import render
from django.views import generic
from .models import Curso

class CursoList(generic.ListView):
    queryset = Curso.objects.order_by('criado_em')
    template_name = 'index.html'
    paginate_by = 5

class CursoDetail(generic.DetailView):
    model = Curso
    template_name = 'curso_detalhes.html'

def sobre(request):
    return render(request, 'sobre.html')