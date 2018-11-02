# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Digitos de verificação do CPF


def calcula_digitos_verificacao(entrada):
    lista_saida = []
    for repeticoes in range(2):
        contador = 2
        soma = 0
        for i in range(len(entrada) - 1, - 1, -1):
            soma += (int(entrada[i]) * contador)
            contador += 1

        digito = (10 * soma) % 11
        if digito == 10:
            digito = 0
        lista_saida.append(digito)
        entrada += str(digito)

    saida = '%i%i' % (lista_saida[0], lista_saida[1])
    return saida