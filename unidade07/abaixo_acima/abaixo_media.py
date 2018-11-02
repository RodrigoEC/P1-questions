# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Abaixo e Acima

def organiza_por_media(lista):
    soma = 0
    for elemento in lista:
        soma += elemento

    if len(lista) > 0:
        media = soma / len(lista)

    else:
        return lista
        
    for i in range(len(lista) - 1, -1, -1):
        for e in range(len(lista) - 1, -1, -1):
            if lista[e] > media:
                lista.append(lista.pop(e))
        
    return lista  