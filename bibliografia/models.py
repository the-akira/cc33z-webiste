from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField

class Livro(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    autor = models.CharField(max_length=200, unique=True)
    registrado_por = models.ForeignKey(User, on_delete= models.CASCADE,related_name='livros')
    capa = models.URLField(max_length=200, default='URL da capa')
    ano_lancamento = models.DateField(null=True, blank=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    registrado_em = models.DateTimeField(auto_now_add=True)
    descricao = MarkdownxField(default='Descrição do livro')

    class Meta:
        ordering = ['ano_lancamento']

    def __str__(self):
        return self.titulo