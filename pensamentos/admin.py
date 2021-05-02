from django.contrib import admin
from .models import Pensamento

class PensamentoAdmin(admin.ModelAdmin):
    list_display = ('autor','registrado_por','registrado_em')
    search_fields = ['autor', 'pensamentos']
  
admin.site.register(Pensamento, PensamentoAdmin)