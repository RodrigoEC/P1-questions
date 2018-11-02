# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Duplas do projeto

def insere_nome(aluno1, lista_duplas, aluno2):
    indice_procurado = len(lista_duplas)
    for i in range(len(lista_duplas)):
        if lista_duplas[i] == aluno2:
            indice_procurado = i
    
    lista_duplas.append(aluno1)
    
    for indice in range(len(lista_duplas) - 1, 0 ,-1):
        if indice == indice_procurado: break
        lista_duplas[indice], lista_duplas[indice - 1] = lista_duplas[indice - 1], lista_duplas[indice]