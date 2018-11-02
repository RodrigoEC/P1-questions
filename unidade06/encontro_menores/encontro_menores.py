# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Encontro Menores

def encontra_menores(num, lista):
    for e in lista:
        if e < num:
            return e
    return -1