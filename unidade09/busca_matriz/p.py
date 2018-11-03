# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Busca em matriz

def busca_matriz(matriz, numero):
    for l in range(len(matriz)):
        for e in range(len(matriz[l])):
            num = matriz[l][e]
            if num == numero:
                return (l, e)
    return