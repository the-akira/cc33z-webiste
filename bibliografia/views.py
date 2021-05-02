from django.views import generic
from .models import Livro

class LivroList(generic.ListView):
    queryset = Livro.objects.order_by('ano_lancamento')
    template_name = 'livros.html'
    paginate_by = 4