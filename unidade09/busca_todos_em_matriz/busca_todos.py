# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Busca Todos

def busca_matriz(matriz, numero):
    lista_saida = []
    for coluna in range(len(matriz)):
        for linha in range(len(matriz[coluna])):
            if matriz[coluna][linha] == numero:
                lista_saida.append((coluna,linha))
  
    return lista_saida