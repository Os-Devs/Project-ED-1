from Campeonato import Campeonato
from Pais import Pais
from Praia import Praias
from Prancha import Prancha
from Surfista import Surfista

if __name__ == '__main__':
    lista_surfistas = []
    camp1 = Campeonato('World Wave', 'John', 'Barramas', 2450, lista_surfistas)
    s1 = Surfista('John', 21)
    s2 = Surfista('Alef', 22)
    lista_surfistas.append(s1)
    lista_surfistas.append(s2)

    print(camp1)