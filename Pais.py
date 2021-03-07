class Pais:
	def __init__(self, nome, lingua):
		self._nome = nome
		self._lingua = lingua
		self._praias = []

	@property
	def nome_do_pais(self):
		return self._nome

	@nome_do_pais.setter
	def nome_do_pais(self, nome_do_pais):
		self._nome = nome_do_pais

	@property
	def linguas(self):
		return self._lingua

	@linguas.setter
	def linguas(self, linguas):
		self._lingua = linguas

	@property
	def praias(self):
		return self._lingua

	@praias.setter
	def praias(self, praias):
		self.praias.append(praias)

	def praias_pais(self, quant):
		praias_pais = ''
		for i in range(len(self._praias)):
			if (self._praias[i].num_camps >= quant):
				praias_pais += self._praias[i].nome_praias

		return praias_pais

	def __str__(self):
		print(f'País: {self._nome}\nLíngua: {self._lingua}')

		for i in range(len(self._praias)):
			print(f'{self._praias[i]}')
	
		return ''