# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Crédito Matrícula

def num_creditos(bd_ufcg, m):
    contador = 0
    for (disciplina) in bd_ufcg:
        for matricula in disciplina:
            if matricula == m:
                contador += 1
    return contador