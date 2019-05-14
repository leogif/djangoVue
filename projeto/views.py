from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	sexo = 'F'
	nome = 'Vue'
	lista = [
		{'nome': 'Leonardo', 'sexo':'m'},
		{'nome': 'Ana Paula', 'sexo':'f'},
		{'nome': 'Bruna', 'sexo':'f'},
		{'nome': 'Renata', 'sexo':'f'},
		{'nome': 'Adriana', 'sexo':'f'},
	]
	return render(request, 'index.html', {'nome': nome, 'sexo': sexo, 'lista': lista})
	
