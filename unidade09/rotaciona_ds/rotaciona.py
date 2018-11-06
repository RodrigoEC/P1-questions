# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Rotaciona diagonal secundaria

def rotaciona_ds(matriz, direcao):
    if direcao == 'cima':
        for linha in range(len(matriz) - 1):
            for numero in range(len(matriz[linha])):
                if linha + numero == len(matriz) - 1:
                    matriz[linha][numero], matriz[linha + 1][numero - 1]\
                    = matriz[linha + 1][numero - 1], matriz[linha][numero]
    
    if direcao == 'baixo':
        for linha in range(len(matriz) - 1, 0, -1):
            for numero in range(len(matriz[linha])):
                if linha + numero == len(matriz) - 1:
                    matriz[linha][numero], matriz[linha - 1][numero + 1]\
                    = matriz[linha - 1][numero + 1], matriz[linha][numero]
