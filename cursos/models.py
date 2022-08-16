from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField

class Curso(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete= models.CASCADE,related_name='cursos')
    material = models.URLField(max_length=200, default='URL do material')
    icone = models.URLField(max_length=200, default='URL do ícone')
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    info = MarkdownxField(default='Informação sobre o curso')
    conteudo = MarkdownxField()

    class Meta:
        ordering = ['criado_em']

    def __str__(self):
        return self.nome