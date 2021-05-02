from django.shortcuts import render
from .models import Contato

def contato(request):
	if request.method == 'POST':
		nome = request.POST.get('nome')
		email = request.POST.get('email')
		mensagem = request.POST.get('mensagem')
		contato = Contato(nome=nome, email=email, mensagem=mensagem)
		contato.save()
	return render(request,'contato.html')
