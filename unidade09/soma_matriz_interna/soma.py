# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Soma matriz interna

def soma_matriz_interna(matriz, inicio, fim):
    soma = 0
    for linha in range(len(matriz)):

        for coluna in range(len(matriz[linha])):

            if (linha >= inicio[0] and linha <= fim[0]) and\
                    (coluna >= inicio[1] and coluna <= fim[1]):
                soma += matriz[linha][coluna]

            elif (linha <= inicio[0] and linha >= fim[0]) and\
                    (coluna <= inicio[1] and coluna >= fim[1]):
                soma += matriz[linha][coluna]
    
    return soma