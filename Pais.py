class Pais:
	def __init__(self, nome, lingua, praias = []):
		self._nome = nome
		self._lingua = lingua
		#self._praias = praias

	@property
	def nome_do_pais (self):
		return self._nome

	@nome_do_pais.setter
	def nome_do_pais (self, nome_do_pais):
		self._nome = nome_do_pais

	@property
	def linguas (self):
		return self._lingua

	@linguas.setter
	def linguas (self, linguas):
		self._lingua = linguas

	# def praias_pais (self):
	# 	return self._praias

	def __str__ (self):
		return (f'País: {self._nome}\nLíngua: {self._lingua}')