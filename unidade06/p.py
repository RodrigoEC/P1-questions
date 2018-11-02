# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Digitos de verificação do CPF

def calcula_digitos_verificacao(entrada):
    lista_saida = []
    for x in range(2):
        contador = 2
        soma = 0
        for i in range(len(entrada) - 1, - 1, -1):
            soma += (int(entrada[i]) * contador)
            contador += 1

        digito = (10 * soma) % 11
        lista_saida.append(digito)
        entrada += str(digito)

    
    return '%i%i' % (lista_saida[0], lista_saida[1])

print calcula_digitos_verificacao('153245875')


