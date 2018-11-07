# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Transporta

def transposta(matriz):
    nova_matriz = []
    lista_aux = []
    for coluna in range(len(matriz[0])):
        for linha in range(len(matriz)):
            lista_aux.append(matriz[linha][coluna])

            if len(lista_aux) == len(matriz):
                nova_matriz.append(lista_aux)
                lista_aux = []
                break

    return nova_matriz