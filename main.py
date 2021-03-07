from Campeonato import Campeonato
from Pais import Pais
from Praia import Praias
from Prancha import Prancha
from Surfista import Surfista
from datetime import date

if __name__ == '__main__':
    pass


    def imprimeMenu():
        print(f'''
                   ALOHA!
        ----------------------------
        | BEM VINDO AO WORLD WAVE  |
        ----------------------------
        |      MENU DE ACESSO      |
        ----------------------------
        |  [1] Acesso ao Cadastro  |
        |  [2] Acesso Campeonatos  |
        |  [3]      Praias         |
        |  [4]    Países-Sedes     |
        |  [5]       SAIR          |\n''')

    lista_campeonatos = []

    imprimeMenu()
    interacao = int(input('Digite qual opção você deseja acessar: '))
    while(interacao != 5):
        if (interacao == 1):
            print('\nCadastro de Surfistas\n')
            name_surfista = input('Insira seu nome: ')
            IdadeSurfista = float(input('Sua Idade: '))
            peso_surfista = float(input('Seu Peso KG: '))
            altura_surfista = float(input('Sua Altura: '))
            cadastro_surfista = Surfista(name_surfista, IdadeSurfista, peso_surfista, altura_surfista)
            cadastro_surfista.campeonatos.append(lista_campeonatos)
            print('Cadastro Realizado com Sucesso!')

            print('\nCadastro de Pranchas\n')
            MarcaPrancha = input('Marca da sua prancha: ')
            Comprimen_Prancha = input('Comprimento da sua prancha: ')
            CorPrancha = input('Cor da sua prancha: ')
            ValorPrancha = input('Valor da sua prancha:$ ')
            FabriPrancha = input('País de fabricação da sua prancha: ')
            cadastro_pranchas = Prancha(MarcaPrancha, Comprimen_Prancha, CorPrancha, ValorPrancha, FabriPrancha)
            print('\nCadastro Realizado com Sucesso!')
            cadastro_surfista.pranchas.append(cadastro_pranchas)

            pro = input('\nVocê é um Surfista Profissional? S/N: ').upper()
            if (pro == 'S'):
                pergunta_add_camp = int(input('Quantos campeonatos você já participou? '))
                for i in range(pergunta_add_camp):
                    nome_camp = input('Nome do campeonato: ')
                    praia_camp = input('Praia que sediou o evento: ')
                    premio_camp = float(input('Valor da premiação:$ '))
                    pergunte_campeao = input(f'Você foi campeão do Campeonato {nome_camp}? S/N: ').upper()
                    if (pergunte_campeao == 'S'):
                        cadastro_camp = Campeonato(nome_camp, cadastro_surfista.nome_surfista, praia_camp, premio_camp)
                        lista_campeonatos.append(cadastro_camp)
                    else:
                        nome_campeao = input('Digite o nome do campeão: ')
                        cadastro_camp = Campeonato(nome_camp, nome_campeao, praia_camp, premio_camp)
                        lista_campeonatos.append(cadastro_camp)
                    print(f'\nCadastro do Campeonato {nome_camp} Realizado com Sucesso!')
            else:
                recomend = input('\nDeseja receber recomendações de pranchas? S/N: ').upper()
                if (recomend == 'S'):
                    print(f'\n{cadastro_surfista.recomendacao()}')
                else:
                    print('Fim do Cadastro')

        if (interacao == 2):
            for i in range(len(lista_campeonatos)):
                print(f'{lista_campeonatos[i]}')


        if (interacao == 3):
            pass
        if (interacao == 4): 
            pass
        imprimeMenu()
        interacao = int(input('Digite qual opção você deseja acessar: '))    
