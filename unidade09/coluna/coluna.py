# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Coluna

def coluna(matriz, indice):
    lista_saida = []
    contador = 0
    while True:
        if contador == len(matriz): break
        
        lista_saida.append(matriz[contador][indice])
        contador += 1

    return lista_saida