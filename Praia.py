class Praias:
	def __init__ (self, nome, num_camps_realizados, pais):
		self._nome = str(nome)
		self._numeros_camps_realizados = int(num_camps_realizados)
		self._pais = str(pais)

	@property
	def nome_praias (self):
		return self._nome

	@nome_praias.setter
	def nome_praias (self, nome_praias):
		self._nome = nome_praias

	@property
	def num_camps (self):
		return self._numeros_camps_realizados

	@num_camps.setter
	def num_camps (self, num_camps):
		self._numeros_camps_realizados = num_camps

	def pais (self, pais):
		self._pais = pais
	
	def __str__(self):
	 	return (f'Nome da praia: {self._nome}\nNúmero de campeonatos realizados na praia: {self._numeros_camps_realizados}'
	 	f'Praia fica em {self._pais}')