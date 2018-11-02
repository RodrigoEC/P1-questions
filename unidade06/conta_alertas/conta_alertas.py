# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Conta Alertas

def conta_alertas_acude(medicoes):
    contador = 0
    for i in range(len(medicoes)):
        diferenca = abs(medicoes[i] - medicoes[i - 1])
        if medicoes[i] < 17 and diferenca < 10:
            contador += 1
    return contador