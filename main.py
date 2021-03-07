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


    def imprimeMenu():
        print(f'''
                   ALOHA!
        ----------------------------
        | BEM VINDO AO WORLD WAVE  |
        ----------------------------
        |      MENU DE ACESSO      |
        ----------------------------
        |  [1] Cadastro Surfista   |
        |  [2] Cadastro Pranchas   |
        |  [3]    Países Sedes     |
        |  [4]      Praias         |
        |  [5]    Campeonato       |
        |  [6]       SAIR          |\n''')



    while(True):
        imprimeMenu()
        interacao = input('Digite qual opção você deseja acessar: ')
        
        break
    
