# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Operações bancárias

nome_saldo = raw_input()
lista = nome_saldo.split()

saldo = float(lista[1])
while True:
    lista_codigos = raw_input().split()
    if lista_codigos[0] == '1':
        saldo -= float(lista_codigos[1])
    elif lista_codigos[0] == '2':
        saldo += float(lista_codigos[1])
    elif lista_codigos[0] == '3':
        break
print 'Saldo de R$ %.2f na conta de %s' % (saldo, lista[0])
