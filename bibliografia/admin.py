from django.contrib import admin
from .models import Livro

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'registrado_por','ano_lancamento','registrado_em')
    search_fields = ['titulo', 'autor','descricao']
  
admin.site.register(Livro, LivroAdmin)