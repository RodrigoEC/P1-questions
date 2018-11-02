# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Distribui Alunos

def distribui_alunos(turma1, turma2, capacidade):
    lista_lab1 = []
    lista_lab2 = []
    lista_auxiliar = []
    while len(turma1) != 0 or len(turma2) != 0:
        if len(turma1) > 0:
            lista_auxiliar.append(turma1[0])
            turma1.pop(0)

        if len(turma2) > 0:
            lista_auxiliar.append(turma2[0])
            turma2.pop(0)
    
    if len(lista_auxiliar) < capacidade:
        for i in range(len(lista_auxiliar) - 2):
                lista_lab1.append(lista_auxiliar[i])

        lista_lab2.append(lista_auxiliar[-1])

    else:
        for i in range(len(lista_auxiliar)):
            if i < capacidade:
                lista_lab1.append(lista_auxiliar[i])

            else:
                lista_lab2.append(lista_auxiliar[i])

    return [lista_lab1, lista_lab2]