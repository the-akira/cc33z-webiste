from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'autor','criado_em')
    search_fields = ['nome', 'conteudo']
    prepopulated_fields = {'slug': ('nome',)}
  
admin.site.register(Curso, CursoAdmin)