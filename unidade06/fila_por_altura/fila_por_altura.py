# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Fila por Altura


def insere_na_fila(fila, nome, altura):
    switch = False
    tupla_entrada = (nome, altura)
    fila.append(fila[-1])
    for i in range(len(fila) - 1):
        tupla = fila[i]
        if tupla[1] >= altura and switch == False:
            v_auxiliar = fila[i]
            fila[i] = tupla_entrada
            switch = True
        
        elif tupla[1] >= altura and switch == True:
            fila[i] = v_auxiliar
            v_auxiliar = tupla

    tupla = fila[-1]
    if tupla[1] < altura:
        fila[-1] = tupla_entrada
           
    return fila