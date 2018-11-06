# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Soma moldura k

def soma_moldura(matriz, nivel):
    soma  = 0
    if len(matriz[0]) != len(matriz):
        return soma
    
    for linha in range(nivel, len(matriz) - nivel):
        for indice in range(nivel,len(matriz[linha]) - nivel):
            if linha == nivel or indice == nivel or \
            linha == len(matriz) - 1 - nivel or indice == len(matriz) - 1 - nivel:
                soma += matriz[linha][indice]
  
    return soma 