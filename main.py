from Campeonato import Campeonato
from Pais import Pais
from Praia import Praias
from Prancha import Prancha
from Surfista import Surfista

if __name__ == '__main__':

    lista_surfistas = []
    lista_praias = []
    lista_pranchas = []
    lista_campeonato = []

    s1 = Surfista('John', 21) #lista_campeonato, lista_pranchas)
    s2 = Surfista('Alef', 22)

    pais1 = Pais()

    camp1 = Campeonato('World Wave', s1.nome_surfista, 'Barramas', 2450, lista_surfistas)
    camp2 = Campeonato('Shake Wave', s2.nome_surfista, 'Hawai', 2600)
    camp3 = Campeonato('Miami Wave', s1.nome_surfista, 'Bahia', 3000)

    p1 = Prancha('Fireside', 2.03, 'Azul', 5000, 'Suiça')
    p2 = Prancha('Fireside', 2.6, 'Vermelho', 6000, 'China')

    praia1 = Praias('Miami Beach', 3, pais1.nome_do_pais)

    lista_campeonato.append(camp1)
    lista_campeonato.append(camp2)
    lista_campeonato.append(camp3)
    lista_pranchas.append(p1)
    lista_pranchas.append(p2)
    lista_surfistas.append(s1)
    lista_surfistas.append(s2)

    print()
    