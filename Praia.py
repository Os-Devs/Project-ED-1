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
	
	def praias_pais (self, quant):
		praias_pais = ''
		for i in range(len(self._praias)):
			if (self._praias[i].num_camps >= quant):
				praias_pais += self._praias[i].nome_praias

		return praias_pais

	def __str__(self):
		print(f'País: {self._nome}\nLíngua: {self._lingua}')

		for i in range (len(self._praias)):
			print(f'{self._praias[i]}')
		
		return str()
