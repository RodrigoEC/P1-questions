# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Crédito Matrícula

def num_creditos(bd_ufcg, matricula):
    contador = 0
    for (disciplina, matri) in bd_ufcg:
        if matri == matricula:
            contador += 1

    return contador