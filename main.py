from Campeonato import Campeonato
from Pais import Pais
from Praia import Praias
from Prancha import Prancha
from Surfista import Surfista

if __name__ == '__main__':

    s1 = Surfista('Michael', 18, 60, 1.80)
    s2 = Surfista('Max', 22, 67, 1.60)

    camp1 = Campeonato('World Wave', 'Max', 'Barramas', 2500)
    camp2 = Campeonato('WSL', 'Michael', 'Barramas', 2500)

    s1.campeonatos.append(camp1)
    s1.campeonatos.append(camp2)

    print(s1)