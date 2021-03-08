from Campeonato import Campeonato
from Pais import Pais
from Praia import Praias
from Prancha import Prancha
from Surfista import Surfista
from datetime import date

if __name__ == '__main__':

    lista_campeonatos = []
    lista_praias = []

    def imprimeMenu():
        print(f'''
                   ALOHA!
        ----------------------------
        | BEM VINDO AO WORLD WAVE  |
        ----------------------------
        |      MENU DE ACESSO      |
        ----------------------------
        |  [1] Acesso ao Cadastro  |
        |  [2]    Praias-Sedes     |
        |  [3]   Cadastrar Camps   |
        |  [4]     Acesso Camps    |
        |  [5]       SAIR          |\n''')

    

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

            pro = input('\nVocê é um Surfista Profissional? S/N: ').upper()
            if (pro == 'N'):
                recomend = input('\nDeseja receber recomendações de pranchas? S/N: ').upper()
                if (recomend == 'S'):
                    print(f'\n{cadastro_surfista.recomendacao()}')

            print('\nCadastro de Pranchas\n')
            MarcaPrancha = input('Marca da sua prancha: ')
            Comprimen_Prancha = input('Comprimento da sua prancha: ')
            CorPrancha = input('Cor da sua prancha: ')
            ValorPrancha = input('Valor da sua prancha: $ ')
            FabriPrancha = input('País de fabricação da sua prancha: ')
            cadastro_pranchas = Prancha(MarcaPrancha, Comprimen_Prancha, CorPrancha, ValorPrancha, FabriPrancha)
            print('\nCadastro Realizado com Sucesso!')
            cadastro_surfista.pranchas.append(cadastro_pranchas)

        imprimeMenu()
        if (interacao == 2):
            pergunta_add_paises = int(input('Há quantos países já foi à campeonato? '))
            for i in range(pergunta_add_paises):
                nome_pais = str(input(f'Digite o nome do país: '))
                idioma_pais = str(input(f'Qual o idioma falado no(a) {nome_pais}: '))
                cadastro_pais = Pais(nome_pais, idioma_pais)
                nome_da_praia = str(input('Digite o nome da praia: '))
                n_camps = int(input('Número de campeonatos realizados na praia: '))
                cadastro_praia = Praias(nome_da_praia, n_camps, cadastro_pais.nome_do_pais)
                cadastro_pais.praias.append(cadastro_praia)
                lista_praias.append(cadastro_pais)
            praias_selecionadas = int(input(f'Gostaria de receber a recomendação das praias que sediam'
            f' mais campeonatos(1-Sim ou 2-Não): '))
            filtro_praias = int(input(f'Filtrar por praias que sediaram até quantos campeonatos: '))
            for i in range(len(lista_praias)):
                print(f'{lista_praias[i].praias_selecionadas(filtro_praias)}')

        imprimeMenu()
        if (interacao == 3):
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
            
                print('Fim do Cadastro')


        if (interacao == 4):
            for i in range(len(lista_campeonatos)):
                print(f'{lista_campeonatos[i]}')