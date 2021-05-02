from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField

class Pensamento(models.Model):
    autor = models.CharField(max_length=200, unique=True)
    registrado_por = models.ForeignKey(User, on_delete= models.CASCADE,related_name='pensamentos')
    autor_foto = models.URLField(max_length=200, default='URL da foto')
    atualizado_em = models.DateTimeField(auto_now=True)
    registrado_em = models.DateTimeField(auto_now_add=True)
    pensamentos = MarkdownxField(default='Pensamentos do Autor')

    class Meta:
        ordering = ['autor']

    def __str__(self):
        return self.autor