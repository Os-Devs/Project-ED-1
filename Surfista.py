class Surfista:
	def __init__(self, nome, idade, campeonatos = [], pranchas = []):
		self._nome = str(nome)
		self._idade = int(idade)
		self._campeonatos = campeonatos
		self._pranchas = pranchas

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

	def total_ganho(self):
		total = 0
		for i in range(len(self._campeonatos)):
			if (self._campeonatos[i].nome_do_campeao == self._nome):
				total += self._campeonatos[i].premio_campeonato
		return total		

	def pranchas_marca(self, marca):
		total_pranchas = ''
		for i in range(len(self._pranchas)):
			if (self._pranchas[i].marca_prancha == marca):
				total_pranchas += (f'\n{self._pranchas[i]}\n')
		return str(total_pranchas)

	def campeonatos(self):
		total_camp = ''
		for i in range(len(self._campeonatos)):
			if (self._campeonatos[i]._campeao == self._nome):
				total_camp += (f'\n{self._campeonatos[i].nome_do_campeonato}')
		return total_camp

	def __str__(self):
		print(f'Nome: {self._nome}\nIdade: {self._idade}')

		for i in range (len(self._campeonatos)):
			print(f'{self._campeonatos[i]}')

		for i in range (len(self._pranchas)):
			print(f'{self._pranchas[i]}')

		return str()

		