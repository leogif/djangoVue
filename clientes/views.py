from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def clientes(request):
	return HttpResponse('Bruna, Rebecca, Alice')

def clientesDetalhe(request, id):
	return HttpResponse(id)

def clientesNome(request, nome):
	return HttpResponse('Olá %s' % nome)
