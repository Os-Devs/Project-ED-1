class Prancha:
    def __init__(self, marca, comprimento, cor, valor, fabricacao):
        self._marca = str(marca)
        self._comprimento = float(comprimento)
        self._cor = str(cor)
        self._valor = float(valor)
        self._fabricacao = str(fabricacao)
    
    @property
    def marca_prancha(self):
        return self._marca
    
    @marca_prancha.setter
    def marca_prancha(self, prancha):
        self._marca = prancha
    
    @property
    def comprimento_prancha(self):
	    return self._comprimento
        
    @comprimento_prancha.setter
    def comprimento_prancha(self, comprimento):
        self._comprimento = comprimento
    
    @property
    def cor_prancha(self):
        return self._cor
    
    @cor_prancha.setter
    def cor_prancha(self, cor):
        self._cor = cor
    
    @property
    def valor_prancha(self):
        return self._valor
    
    @valor_prancha.setter
    def valor_prancha(self, valor):
        self._valor = valor
    
    @property
    def fabricacao_prancha(self):
        return self._fabricacao
    
    @fabricacao_prancha.setter
    def fabricacao_prancha(self, fabricacao):
        self._fabricacao = fabricacao
    
    def __str__(self):
        return (f'Marca {self._marca}\nComprimento: {self._comprimento} m\nCor: {self._cor}'
        f'\nValor: R$ {self._valor}\nPaís de fabricação: {self._fabricacao}')