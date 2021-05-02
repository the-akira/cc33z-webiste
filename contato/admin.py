from django.contrib import admin
from .models import Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data')
    search_fields = ['nome', 'mensagem']
  
admin.site.register(Contato, ContatoAdmin)
