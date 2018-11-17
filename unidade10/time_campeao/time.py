# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Time campeão 

def time_campeao(dados):
    lista_campeoes = []
    campeao = [0, 0, 0]

    for time, tabela in dados.items():

        if tabela[0] > campeao[0]:
            campeao = tabela
            lista_campeoes = []
            lista_campeoes.append(time)
        
        elif tabela[0] == campeao[0]:
            
            lista_campeoes.append(time)
    
    return lista_campeoes