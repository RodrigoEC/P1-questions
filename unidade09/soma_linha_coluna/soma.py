# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Soma linha e coluna

def soma_linha_e_coluna(matriz, l, c):
    soma = 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if linha == l and c != coluna:
                soma += matriz[l][coluna]
            
            elif coluna == c and linha != l:
                soma += matriz[linha][c]
    
    return soma



