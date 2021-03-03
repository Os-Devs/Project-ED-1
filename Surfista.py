from Prancha import *
from Campeonato import *

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

	def surfista_camps(self):
		return self._campeonatos

	def prancha_surfista(self):
		return self._pranchas

