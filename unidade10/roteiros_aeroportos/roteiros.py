# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Roteiros Aeroportos

def my_in(lista, elemento):
    for e in lista:
        if e == elemento:
            return True

    return False


def eh_roteiro(iata, voos, roteiro):
    lista_lugares = roteiro.split("/")

    for i in range(len(lista_lugares) - 1):
        partida = lista_lugares[i]
        destino = lista_lugares[i + 1]
        
        if my_in(voos[iata[partida]], iata[destino]) == False:
            return False 

    return True