from django.views import generic
from .models import Pensamento

class PensamentoList(generic.ListView):
    queryset = Pensamento.objects.order_by('autor')
    template_name = 'pensamentos.html'
    paginate_by = 4