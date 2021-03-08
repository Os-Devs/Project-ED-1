from Campeonato import Campeonato
from Pais import Pais
from Praia import Praias
from Prancha import Prancha
from Surfista import Surfista
from datetime import date

if __name__ == '__main__':

    lista_Campeonatos = []
    lista_Pranchas = []
    lista_Surfistas = []
    lista_Praias = []
    lista_Pais = []

    surfsNome = ['John', 'Abner','Vinicius','Alef','Eduardo','Italo','Mael']

    surfirsta1 = Surfista(surfsNome[0], 18, 60, 1.60)
    surfirsta2 = Surfista(surfsNome[1], 20, 59, 1.67)
    surfirsta3 = Surfista(surfsNome[2], 19, 62, 1.70)
    surfirsta4 = Surfista(surfsNome[3], 21, 65, 1.72)
    surfirsta5 = Surfista(surfsNome[4], 23, 72, 1.80)
    surfirsta6 = Surfista(surfsNome[5], 30, 58, 1.77)
    surfirsta7 = Surfista(surfsNome[6], 17, 70, 1.85)

    lista_Surfistas.append(surfirsta1)
    lista_Surfistas.append(surfirsta2)
    lista_Surfistas.append(surfirsta3)
    lista_Surfistas.append(surfirsta4)
    lista_Surfistas.append(surfirsta5)
    lista_Surfistas.append(surfirsta6)
    lista_Surfistas.append(surfirsta7)

    praiasNome = ['Côte des Basques','Banzai Pipeline','Pipa','Mavericks','Hossegor','Maracaípe','Cloudbreak']

    praia1 = Praias(praiasNome[0], 2)
    praia2 = Praias(praiasNome[1], 4)
    praia3 = Praias(praiasNome[2], 10)
    praia4 = Praias(praiasNome[3], 5)
    praia5 = Praias(praiasNome[4], 3)
    praia6 = Praias(praiasNome[5],7)
    praia7 = Praias(praiasNome[6], 12)

    lista_Praias.append(praia1)
    lista_Praias.append(praia2)
    lista_Praias.append(praia3)
    lista_Praias.append(praia4)
    lista_Praias.append(praia5)
    lista_Praias.append(praia6)
    lista_Praias.append(praia7)


    campsNomes = ['World Wave', 'Surf Wave', 'Wave', 'WSL', 'Storm Wave', 'Surf life', 'Surf Real']


    camp1 = Campeonato(campsNomes[0], surfirsta1.nome_surfista, praia1.nome_praias, 2500)
    camp2 = Campeonato(campsNomes[1], surfirsta2.nome_surfista, praia2.nome_praias, 2700)
    camp3 = Campeonato(campsNomes[2], surfirsta3.nome_surfista, praia3.nome_praias, 3500)
    camp4 = Campeonato(campsNomes[3], surfirsta4.nome_surfista, praia4.nome_praias, 3000)
    camp5 = Campeonato(campsNomes[4], surfirsta5.nome_surfista, praia5.nome_praias, 3100)
    camp6 = Campeonato(campsNomes[5], surfirsta6.nome_surfista, praia6.nome_praias, 2000)
    camp7 = Campeonato(campsNomes[6], surfirsta7.nome_surfista, praia7.nome_praias, 2800)

    lista_Campeonatos.append(camp1)
    lista_Campeonatos.append(camp2)
    lista_Campeonatos.append(camp3)
    lista_Campeonatos.append(camp4)
    lista_Campeonatos.append(camp5)
    lista_Campeonatos.append(camp6)
    lista_Campeonatos.append(camp7)

    paisNome = ['Brasil','Espanha','Portugal','Chile','Holanda','Alemão','França']
    paisIdiomas = ['Português-BR', 'Espanhol', 'Português-PT', 'Espanhol', 'Holandês', 'Alemanha','Francês']

    pais1 = Pais(paisNome[0], paisIdiomas[0])
    pais2 = Pais(paisNome[1], paisIdiomas[1])
    pais3 = Pais(paisNome[2], paisIdiomas[2])
    pais4 = Pais(paisNome[3], paisIdiomas[3])
    pais5 = Pais(paisNome[4], paisIdiomas[4])
    pais6 = Pais(paisNome[5], paisIdiomas[5])
    pais7 = Pais(paisNome[6], paisIdiomas[6])

    lista_Pais.append(pais1)
    lista_Pais.append(pais2)
    lista_Pais.append(pais3)
    lista_Pais.append(pais4)
    lista_Pais.append(pais5)
    lista_Pais.append(pais6)
    lista_Pais.append(pais7)

    pranchaNome = ['Firewire','Lost','DHD Surfboards','Hayden Shapes','Pukas','Mick Fanning Softboards','NSP Surfboards',]
    pranchaCor = ['Verde','Azul','Magenta','Amarelo','Vermelho','Laranja','Branco']

    prancha1 = Prancha(pranchaNome[0], 2.75, pranchaCor[0],  2300, pais1.nome_do_pais)
    prancha2 = Prancha(pranchaNome[1], 2.15, pranchaCor[1],  2300, pais2.nome_do_pais)
    prancha3 = Prancha(pranchaNome[2], 2.43, pranchaCor[2],  2300, pais3.nome_do_pais)
    prancha4 = Prancha(pranchaNome[3], 2.07, pranchaCor[3],  2300, pais4.nome_do_pais)
    prancha5 = Prancha(pranchaNome[4], 2.33, pranchaCor[4],  2300, pais5.nome_do_pais)
    prancha6 = Prancha(pranchaNome[5], 2.72, pranchaCor[5],  2300, pais6.nome_do_pais)
    prancha7 = Prancha(pranchaNome[6], 2.45, pranchaCor[6],  2300, pais7.nome_do_pais)

    lista_Pranchas.append(prancha1)
    lista_Pranchas.append(prancha2)
    lista_Pranchas.append(prancha3)
    lista_Pranchas.append(prancha4)
    lista_Pranchas.append(prancha5)
    lista_Pranchas.append(prancha6)
    lista_Pranchas.append(prancha7)


    lista_Campeonatos[0].surfistas.append(surfirsta1)
    lista_Campeonatos[0].surfistas.append(surfirsta3)
    lista_Campeonatos[0].surfistas.append(surfirsta5)
    lista_Campeonatos[0].surfistas.append(surfirsta7)

    lista_Campeonatos[1].surfistas.append(surfirsta2)
    lista_Campeonatos[1].surfistas.append(surfirsta4)
    lista_Campeonatos[1].surfistas.append(surfirsta6)
    lista_Campeonatos[1].surfistas.append(surfirsta7)

    lista_Campeonatos[2].surfistas.append(surfirsta3)
    lista_Campeonatos[2].surfistas.append(surfirsta4)
    lista_Campeonatos[2].surfistas.append(surfirsta5)
    lista_Campeonatos[2].surfistas.append(surfirsta6)

    lista_Campeonatos[3].surfistas.append(surfirsta1)
    lista_Campeonatos[3].surfistas.append(surfirsta2)
    lista_Campeonatos[3].surfistas.append(surfirsta3)
    lista_Campeonatos[3].surfistas.append(surfirsta4)

    lista_Campeonatos[4].surfistas.append(surfirsta2)
    lista_Campeonatos[4].surfistas.append(surfirsta4)
    lista_Campeonatos[4].surfistas.append(surfirsta5)
    lista_Campeonatos[4].surfistas.append(surfirsta7)

    lista_Campeonatos[5].surfistas.append(surfirsta1)
    lista_Campeonatos[5].surfistas.append(surfirsta4)
    lista_Campeonatos[5].surfistas.append(surfirsta6)
    lista_Campeonatos[5].surfistas.append(surfirsta7)

    lista_Campeonatos[6].surfistas.append(surfirsta2)
    lista_Campeonatos[6].surfistas.append(surfirsta4)
    lista_Campeonatos[6].surfistas.append(surfirsta6)
    lista_Campeonatos[6].surfistas.append(surfirsta7)

    lista_Surfistas.append(lista_Campeonatos)

    def participantes(nome_camp):
        participantes = ''

        for i in range(len(lista_Campeonatos)):
            if (lista_Campeonatos[i].nome_do_campeonato == nome_camp):
                participantes += (lista_Campeonatos[i].participantes())
        
        return participantes

    def camp_menorIdade():
        menorIdade = 999
        for i in range(len(lista_Campeonatos)):
            if (lista_Campeonatos[i].menor_idade() < menorIdade):
                menorIdade = (lista_Campeonatos[i].menor_idade())
        
                output_menorIdade = (f'{lista_Campeonatos[i].nome_do_campeao} {menorIdade} anos')

        return output_menorIdade

    def camp_maiorIdade():
        maiorIdade = 0
        for i in range(len(lista_Campeonatos)):
            if (lista_Campeonatos[i].maior_idade() > maiorIdade):
                maiorIdade = (lista_Campeonatos[i].maior_idade())
        
                output_maiorIdade = (f'{lista_Campeonatos[i].nome_do_campeao} {maiorIdade} anos')

        return output_maiorIdade
