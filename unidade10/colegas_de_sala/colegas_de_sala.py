# coding: utf-8

################################################
# Disciplina: Programação 01 - 2018.1          #
# Nome: Rodrigo Eloy Cavalcanti                #
# Matrícula: 118210111                         #
# E-mail: rodrigo.cavalcanti@ccc.ufcg.edu.br   #
# Atividade: Colegas de Sala                   #
# Unidade: 10                                  #
################################################


def colegas_de_sala(profs_salas, prof):
    professores_mesma_sala = []

    sala_prof = profs_salas[prof]
    for (professor, sala) in profs_salas.items():
        if sala == sala_prof and professor != prof:
            professores_mesma_sala.append(professor)
    
    return professores_mesma_sala
        