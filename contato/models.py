from django.db import models

class Contato(models.Model):
  nome = models.CharField(max_length=122)
  email = models.CharField(max_length=120)
  data = models.DateTimeField(auto_now_add=True)
  mensagem = models.TextField()
