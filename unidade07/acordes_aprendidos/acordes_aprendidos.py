# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Acordes aprendidos

def acordes(m1, m2):
    lista_saida = []
    for acorde in m1:
        lista_saida.append(acorde)

    lista_auxiliar = []
    for acorde in m2:
        lista_auxiliar.append(acorde)

    for e in range(len(lista_saida) - 1, -1 , -1):
        for i in range(len(lista_auxiliar) - 1, -1, -1):
            if lista_auxiliar[i] == lista_saida[e]:
                lista_auxiliar.pop(i)
                
    lista_saida += lista_auxiliar
    
    return lista_saida