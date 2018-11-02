# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Divisor

def divisor(num, lista):
    saida = -1
    for i in range(len(lista)):
        if lista[i] % num == 0 or num % lista[i] == 0:
            saida = i
            break
    return saida
