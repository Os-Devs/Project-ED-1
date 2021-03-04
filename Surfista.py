class Surfista:
	def __init__(self, nome, idade, campeonatos = [], pranchas = []):
		self._nome = str(nome)
		self._idade = int(idade)
		self._campeonatos = campeonatos
		self._pranchas = pranchas
		self._total_ganho = []

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

	def totalganho(self):
		total = 0
		for i in range(len(self._campeonatos)):
			total += self._campeonatos

	def __str__(self):
		return (f'Nome: {self._nome}\nIdade: {self._idade}')
		