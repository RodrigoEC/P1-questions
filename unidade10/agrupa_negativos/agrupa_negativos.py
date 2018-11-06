# coding: utf-8

################################################
# Disciplina: Programação 01 - 2018.1          #
# Nome: Rodrigo Eloy Cavalcanti                #
# Matrícula: 118210111                         #
# E-mail: rodrigo.cavalcanti@ccc.ufcg.edu.br   #
# Atividade: Agrupa negativos                  #
# Unidade: 10                                  #
################################################

def agrupa_negativos(lista):
    num_agrupados = {
        "nao-negativos": [],
        "negativos": []
    }

    for numero in lista:
        if numero < 0:
            num_agrupados["negativos"].append(numero)
        else:
            num_agrupados["nao-negativos"].append(numero)
    
    return num_agrupados
