from Surfista import *

class Campeonato:
	def __init__ (self, nome_campeonato, campeao, praia, premio, surfistas):
		self._nome_campeonato = str(nome_campeonato)
		self._campeao = str(campeao)
		self._praia = str(praia)
		self._premio = float(premio)
		self._surfistas = str(surfistas)

	@property
	def nome_do_campeonato (self):
		return self._nome_campeonato

	@nome_do_campeonato.setter
	def nome_do_campeonato (self, nome_do_campeonato):
		self._nome_campeonato = nome_do_campeonato

	@property
	def nome_do_campeao (self):
		return self._campeao

	@nome_do_campeao.setter
	def nome_do_campeao (self, nome_do_campeao):
		self._campeao = nome_do_campeao

	@property
	def praia_do_campeonato (self):
		return self._praia

	@praia_do_campeonato.setter
	def praia_do_campeonato (self, praia_do_campeonato):
		self._praia = praia_do_campeonato

	@property
	def premio_campeonato (self):
		return self._premio

	@premio_campeonato.setter
	def premio_campeonato (self, premio_campeonato):
		self._premio = premio_campeonato

	@property
	def surfistas_do_campeonato (self):
		return self._surfistas

	@surfistas_do_campeonato.setter
	def surfistas_do_campeonato (self, surfistas_do_campeonato):
		self._surfistas = surfistas_do_campeonato
      