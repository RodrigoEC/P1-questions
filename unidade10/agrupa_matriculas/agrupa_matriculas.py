# coding: utf-8

################################################
# Disciplina: Programação 01 - 2018.1          #
# Nome: Rodrigo Eloy Cavalcanti                #
# Matrícula: 118210111                         #
# E-mail: rodrigo.cavalcanti@ccc.ufcg.edu.br   #
# Atividade: Agrupa Matrículas                 #
# Unidade: 10                                  #
################################################

def get_periodo(matricula):
    return matricula[0] + matricula[1] + matricula[2]

def agrupa_por_periodo(turma):
    agrupa_por_matricula = {}
    
    for matricula in turma:
        periodo = get_periodo(matricula)

        if agrupa_por_matricula.has_key(periodo):
            agrupa_por_matricula[periodo] += 1
        else:
            agrupa_por_matricula[periodo] = 1
    
    return agrupa_por_matricula