# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Anula

def anula(lista):
    for e in range(len(lista) - 1):
        for i in range(len(lista) -1, 0, -1):
            if lista[i] + lista[i - 1] == 0:
                lista.pop(i), lista.pop(i - 1)
                break