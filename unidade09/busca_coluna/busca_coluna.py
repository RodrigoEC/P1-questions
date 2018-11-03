# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Busca por coluna

def busca_todos_por_coluna_em_matriz(matriz, numero):
    lista_saida = []
    coluna = 0
    linha = 0
    while True:
        if matriz[coluna][linha] == numero:
            lista_saida.append((coluna, linha))

        coluna += 1

        if coluna == len(matriz) - 1 and linha != len(matriz[0]) - 1:
            if matriz[coluna][linha] == numero:
                lista_saida.append((coluna, linha))
            linha += 1
            coluna = 0

        elif coluna == len(matriz) - 1 and linha == len(matriz[0]) - 1: 
            if matriz[-1][-1] == numero:
                lista_saida.append((coluna, linha))
            break

    return lista_saida