# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Número de disciplinas

def comparador_listas(lista1, lista2):
    contador = 0
    for e in lista1:
        for elemento in lista2:
            if elemento == e:
                contador += 1
    
    if contador == len(lista2):
        return True
    
    return False

def my_in(lista, elemento):
    for e in lista:
        if e == elemento:
            return True
    return False


def numero_disciplinas(grade, horario, cadeiras_pagas):
    lista_horarios = []
    matriculaveis = 0
    for cadeira, pre_requisitos in grade.items():
        if comparador_listas(cadeiras_pagas, pre_requisitos) and\
         my_in(cadeiras_pagas, cadeira) == False:
            matriculaveis += 1
        
            if my_in(lista_horarios, horario[cadeira]):
                matriculaveis -= 1
            lista_horarios.append(horario[cadeira])
    
    return matriculaveis