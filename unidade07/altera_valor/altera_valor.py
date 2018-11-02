# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Altera Valor

def altera_vetor_por_escalar(vetor, escalar):
    for i in range(len(vetor)):
        multi_escalar = vetor[i] * escalar
        vetor[i] = multi_escalar