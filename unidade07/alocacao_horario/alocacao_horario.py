# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Alocação Horário


def get_choque_horario(cronograma):
    lista_saida = []
    contador = 0
    for i in range(len(cronograma)):
        disciplina = cronograma[i]
        contador = 0

        for cadeira in cronograma:
            if cadeira[-1] == disciplina[-1]:
                contador += 1
            
            if contador == 2:
                lista_saida.append(cronograma[i])
                contador = 0
        
        for e in range(len(lista_saida) - 1, 0, -1):
            disciplina = lista_saida[e]
            prox_disciplina = lista_saida[e - 1]
            if int(disciplina[-1]) < int(prox_disciplina[-1]):
                lista_saida[e], lista_saida[e - 1] = lista_saida[e - 1], lista_saida[e]

    return lista_saida