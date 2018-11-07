# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Pi por aproximações

erro = float(raw_input())
switch = True
contador = 0
pi = 0
while True:
    if switch == True:
        divisor = 1 + contador
        switch = False
        pi_ant = 4 * (1.0 / divisor)
    else:
        divisor = -1 * (1 + contador)
        pi_ant = -4 * (1.0 / divisor)
        switch = True

    pi = 4 * (1.0 / divisor + (pi / 4.0))
    
    print '%.6f' % pi
    if pi_ant < erro:
        break
    contador += 2