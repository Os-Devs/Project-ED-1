class Surfista:
	def __init__(self, nome, idade, peso, altura):
		self._nome = str(nome)
		self._idade = int(idade)
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

	def total_ganho(self):
		total = 0
		for i in range(len(self._campeonatos)):
			if (self._campeonatos[i].nome_do_campeao == self._nome):
				total += self._campeonatos[i].premio_campeonato
		return total

	def campeonatos_ganhos(self):
		total_camp = ''
		for i in range(len(self._campeonatos)):
			if (self._campeonatos[i]._campeao == self._nome):
				total_camp += (f'\n{self._campeonatos[i].nome_do_campeonato}')
		return total_camp

	def pranchas_marca(self, marca):
		total_pranchas = ''
		for i in range(len(self._pranchas)):
			if (self._pranchas[i].marca_prancha == marca):
				total_pranchas += (f'\n{self._pranchas[i]}\n')
		return str(total_pranchas)
	
	def recomendacao(self):
		pass

	def __str__(self):
		output_surfista = (f'\nNome: {self._nome}\nIdade: {self._idade}')

		for i in range (len(self._campeonatos)):
			output_surfista += (f'\n{self._campeonatos[i]}')

		for i in range (len(self._pranchas)):
			output_surfista += (f'{self._pranchas[i]}')

		return output_surfista