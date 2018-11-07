# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Diagonais

def diagonais(matriz):
    lista_diagonal_principal = []
    lista_diagonal_secundaria = []
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):

            numero = matriz[linha][coluna]
            if linha == coluna:
                lista_diagonal_principal.append(numero)
            
            if linha + coluna == len(matriz) - 1:
                lista_diagonal_secundaria.append(numero)
        
    nova_matriz = [lista_diagonal_principal, lista_diagonal_secundaria]

    return nova_matriz