# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Conta energia

def calcula_conta(tabela):
    soma = 0
    for linha in range(1, len(tabela)):
        quant = float(tabela[linha][1]) * tabela[linha][2]* tabela[linha][3] / 1000
        soma += quant

    saida = soma * 0.28
    return "R$ %.2f" % saida