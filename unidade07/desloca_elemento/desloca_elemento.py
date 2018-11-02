# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Desloca Elemento

def desloca(lista, origem, destino):
    num_origem = lista.pop(origem)
    lista.append(num_origem)
    
    for i in range(len(lista) - 1, 0, -1):
        if i == destino: break
        lista[i], lista[i - 1] = lista[i - 1], lista[i]