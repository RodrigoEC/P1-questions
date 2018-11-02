# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Agrupa Próximos


def agrupa_proximos(lista, valor, criterio):
    lista_nova = []     
    for numero in lista:
        if numero < valor:
            if valor - numero < criterio:
                lista_nova.append(numero)
        else:
            if numero - valor < criterio:
                lista_nova.append(numero)    
    return lista_nova   

