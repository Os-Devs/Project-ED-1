from datetime import date

class Campeonato:
	def __init__(self, nome_campeonato, campeao, praia, premio):
		self._nome_campeonato = str(nome_campeonato)
		self._campeao = str(campeao)
		self._praia = str(praia)
		self._premio = float(premio)
		self._surfistas = []
		self._datas = []

	@property
	def nome_do_campeonato(self):
		return self._nome_campeonato

	@nome_do_campeonato.setter
	def nome_do_campeonato(self, nome_do_campeonato):
		self._nome_campeonato = nome_do_campeonato

	@property
	def nome_do_campeao(self):
		return self._campeao

	@nome_do_campeao.setter
	def nome_do_campeao(self, nome_do_campeao):
		self._campeao = nome_do_campeao

	@property
	def praia_do_campeonato(self):
		return self._praia

	@praia_do_campeonato.setter
	def praia_do_campeonato(self, praia_do_campeonato):
		self._praia = praia_do_campeonato

	@property
	def premio_campeonato(self):
		return self._premio

	@premio_campeonato.setter
	def premio_campeonato(self, premio_campeonato):
		self._premio = premio_campeonato
	
	@property
	def surfistas(self):
		return self._surfistas
	
	@surfistas.setter
	def surfistas(self, surfistas):
		self._surfistas.append(surfistas)

	@property
	def data(self):
		return self._datas
	
	@data.setter
	def data(self, data):
		self._datas.append(data)

	def menor_idade(self):
		idade_min = 99
		for i in range(len(self._surfistas)):
			if (self._surfistas[i].idade_surfista < idade_min):
				idade_min = (self._surfistas[i].idade_surfista)
		return idade_min

	def maior_idade(self):
		idade_max = 0
		for i in range(len(self._surfistas)):
			if (self._surfistas[i].idade_surfista > idade_max):
				idade_max = (self._surfistas[i].idade_surfista)
		return idade_max

	def datas_camps(self, datas):
		datas_camps = ''

		for i in range(len(self._datas)):
			if (date.today() < datas):
				datas_camps += datas
		
		return datas_camps
	
	def participantes(self):
		participantes = ''
		for i in range(len(self._surfistas)):
			participantes += (f'\n{self._surfistas[i].nome_surfista}')
		
		return participantes

	def __str__(self):
		output_campeonato = (f'\nNome do campeonato: {self._nome_campeonato}\nNome do campeão: {self._campeao}'
		f'\nPraia: {self._praia}\nPrêmio: R$ {self._premio:.2f}')
    	
		return output_campeonato