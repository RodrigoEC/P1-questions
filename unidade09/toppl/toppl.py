# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Toppl

def my_in(lista, elemento):
    for e in lista:
        if elemento == e:
            return True

    return False

def filtra_alunos(alunos, inscritos, media):
    contador = 0
    for tupla in range(len(alunos) -1, -1, -1):
        if my_in(inscritos, alunos[tupla][0]) == False or alunos[tupla][1] < media:
            alunos.pop(tupla)
            contador += 1

    return contador