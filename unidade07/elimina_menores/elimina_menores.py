# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Elimina menores

def elimina_menores(num, lista):
    contador = 0
    for i in range(len(lista) -1 , -1 , -1):
        if lista[i] < num:
            lista.pop(i)
            contador += 1
    
    return contador