# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Ajeita Lista

def ajeita_lista(lista):
    def impar(a): return a % 2 != 0
    def par(a): return a % 2 == 0

    for e in range(len(lista) - 1, -1, -1):
        for i in range(len(lista) - 1, 0 , -1):
            if par(lista[i]) and impar(lista[i - 1]) or \
            impar(lista[i]) and impar(lista[i - 1]) and lista[i] < lista[i - 1] or \
            par(lista[i]) and par(lista[i - 1]) and lista[i] > lista[i - 1]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]