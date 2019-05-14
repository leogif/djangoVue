from django.db import models

class Departamento(models.Model):
	nome = models.CharField(max_length=100)
	def __str__(self):
		return self.nome

class CPF(models.Model):
	numero = models.CharField(max_length=11)
	dataExp = models.DateTimeField(auto_now=False)
	# Data de Expedição = dataExp
	def __str__(self):
		return self.numero

class Empregado(models.Model):
	nome = models.CharField(max_length=80, null=False)
	endereco = models.CharField(max_length=200, blank=False, null=False)
	salario = models.DecimalField(max_digits=10, decimal_places=2)
	idade = models.IntegerField()
	email = models.EmailField()
	cpf = models.OneToOneField(CPF, blank=True, null=True)
	funcao = models.CharField(max_length=120, null=False)
	departamentos = models.ManyToManyField(Departamento, blank=True)
	foto = models.ImageField(upload_to='fotoEmpregado')
	# blank, deixa explicito que o campo pode ficar em branco. Null = True
	# Django reclamou que o Null não tem efeito em ManyToMany

	def __str__(self):
		return self.nome

class Telefone(models.Model):
	numero = models.CharField(max_length=20)
	descricao = models.CharField(max_length=80)
	nomeEmpregado = models.ForeignKey(Empregado)

	def __str__(self):
		return self.descricao + ' - ' + self.numero
	# Concatenação semelhante ao do Javascript