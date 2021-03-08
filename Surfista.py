class Surfista:
	def __init__(self, nome, idade, peso, altura):
		self._nome = str(nome)
		self._idade = int(idade)
		self._peso = float(peso)
		self._altura = float(altura)
		self._campeonatos = []
		self._pranchas = []

	@property
	def nome_surfista(self):
		return self._nome

	@nome_surfista.setter
	def nome_surfista(self, nome_surfista):
		self._nome = nome_surfista

	@property
	def idade_surfista(self):
		return self._idade

	@idade_surfista.setter
	def idade_surfista(self, idade_surfista):
		self._idade = idade_surfista

	@property
	def altura(self):
		return self._altura
	
	@altura.setter
	def altura(self, altura):
		self._altura = altura

	@property
	def peso(self):
		return self._peso
	
	@peso.setter
	def peso(self, peso):
		self._peso = peso
	
	@property
	def campeonatos(self):
		return self._campeonatos
	
	@campeonatos.setter
	def campeonatos(self, campeonatos):
		self._campeonatos.append(campeonatos)

	@property
	def pranchas(self):
		return self._campeonatos
	
	@pranchas.setter
	def pranchas(self, pranchas):
		self._pranchas.append(pranchas)

	@property
	def peso(self):
		return self._peso 
	
	@peso.setter
	def peso(self, peso):
		self._peso = peso

	@property
	def altura(self):
		return self._altura
	
	@altura.setter
	def altura(self, altura):
		self._altura = altura

	def total_ganho(self):
		total = 0
		for i in range(len(self._campeonatos)):
			if (self._campeonatos[i].nome_do_campeao == self._nome):
				total += self._campeonatos[i].premio_campeonato
		return total

	def campeonatos_participados(self):
		participou = ''
		for i in range(len(self._campeonatos)):
			participou += (f'\n{self._campeonatos[i].nome_do_campeonato}')
		return participou

	def pranchas_marca(self, marca):
		total_pranchas = ''
		for i in range(len(self._pranchas)):
			if (marca in self._pranchas[i].marca_prancha):
				total_pranchas += (f'\n{self._pranchas[i]}')
		return total_pranchas
	
	def recomendacao(self):
		if (self._peso < 60):
			recomendacao = (f'Volume Ideal: Em torno dos 40L')
		elif (self._peso >= 60 and self._peso < 80):
			recomendacao = (f'Volume Ideal: Entre 42L e 48L')
		else:
			recomendacao = (f'Volume Ideal: Mais de 48L')

		if (self._altura < 1.60):
			recomendacao += (f'\nTamanho Ideal: Menor que 7´0"')
		elif (self._altura >= 1.60 and self._altura < 1.80):
			recomendacao += (f'\nTamanho Ideal: Entre 7´0" e 7´8"')
		else:
			recomendacao += (f'\nTamanho Ideal: Maior ou igual a 7´8"')
		
		return recomendacao

	def __str__(self):
		output_surfista = (f'\nNome: {self._nome}\nIdade: {self._idade}\nPeso: {self._peso}Kg'
		f'\nAltura: {self._altura}m')

		return output_surfista