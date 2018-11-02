# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Caixa Registradora

def caixa_registradora(l_vendas, meta):
    soma = 0
    comissao = 0
    for venda in l_vendas:
        soma += venda
        if venda < 1000:
            comissao += (venda * 5) / 100

        elif venda >= 1000 and venda < 5000:
            comissao += venda / 10

        else:
            comissao += (venda * 15) / 100

    lista_saida = [soma, comissao]
    lucro = soma - comissao
    if lucro < meta:
        lista_saida.append('Prejuizo')

    elif lucro >= meta:
        lista_saida.append('Lucro')
    
    return lista_saida