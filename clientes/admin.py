from django.contrib import admin
from .models import Departamento, CPF, Empregado, Telefone

# fields
# list_display
# list_filter
# search_fields

class EmpregadoAdmin(admin.ModelAdmin):
	# Não coloquei o fields, pois quero todos os campos 
	# para o usuario fazer cadastro.
	list_display = ('id','nome','endereco','email','salario')
	list_filter = ('departamentos',)
	search_fields = ('id','nome')


admin.site.register(Departamento)
admin.site.register(CPF)
admin.site.register(Empregado, EmpregadoAdmin)
admin.site.register(Telefone)
