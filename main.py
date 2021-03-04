from Campeonato import Campeonato
from Pais import Pais
from Praia import Praias
from Prancha import Prancha
from Surfista import Surfista

if __name__ == '__main__':
    lista_surfistas = []
    lista_pranchas = []
    lista_pranchas = []
    lista_campeonato = []

    s1 = Surfista('John', 21, lista_campeonato, lista_pranchas)
    s2 = Surfista('Alef', 22)

    camp1 = Campeonato('World Wave', s1._nome, 'Barramas', 2450)
    camp2 = Campeonato('Shake Wave', s2._nome, 'Hawai', 2600)
    camp3 = Campeonato('Miami Wave', s1._nome, 'Bahia', 3000)

    
    p1 = Prancha('Fireside', '2.03', 'Azul', 5000, 'Suiça')

    lista_campeonato.append(camp1)
    lista_campeonato.append(camp2)
    lista_campeonato.append(camp3)

    lista_pranchas.append(p1)

    print(s1)
    print(s1.campeonatos())