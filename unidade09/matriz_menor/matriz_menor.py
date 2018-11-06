# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Matriz menor


def matriz_menor(matriz1, matriz2):
    lista_aux = []
    lista_saida = []
    for linha in range(len(matriz1)):
        for numero in range(len(matriz1[linha])):
            if matriz1[linha][numero] <= matriz2[linha][numero]:
                lista_aux.append(matriz1[linha][numero])

            else:
                lista_aux.append(matriz2[linha][numero])

    contador = 1
    num_de_listas = (len(lista_aux) / len(matriz1))
    lista_provisoria = []
    for numero in lista_aux:
        lista_provisoria.append(numero)
        
        if contador % num_de_listas == 0:
            lista_saida.append(lista_provisoria)
            lista_provisoria = []
            
        contador += 1

    return lista_saida