# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Cálculo de Seguro

def calcula_seguro(valor, lista):

    pontos = 0
    if lista[0] <= 21 or lista[0] > 60:
        pontos += 20
    elif lista[0] >= 22 and lista[0] <= 30:
        pontos += 15
    elif lista[0] >= 31 and lista[0] <= 40:
        pontos += 12
    elif lista[0] >= 41 and lista[0] <= 60:
        pontos += 10

    if lista[1] == True:
        pontos += 10
    else:
        pontos += 20
        
    if lista[2] == True:
        pontos += 20
    else:
        pontos += 10

    if lista[3] == True:
        pontos += 20
    else:
        pontos += 10
        
    if lista[4] == True:
        pontos += 20
    else:
        pontos += 10
        
    if lista[5] == True:
        pontos += 10
    else:
        pontos += 20
        
    if lista[6] == 'Trabalho':
        pontos += 10
    elif lista[6] == 'Lazer' or lista[6] == 'Misto':
        pontos += 20
    
    lista_saida = [pontos,]
    if pontos <= 80:
        lista_saida.append('Risco Baixo')
        banco_paga = valor / 10
        lista_saida.append(banco_paga)

    elif pontos > 80 and pontos <= 100:
        lista_saida.append('Risco Medio')
        banco_paga = (valor * 2) / 10
        lista_saida.append(banco_paga)

    else:
        lista_saida.append('Risco Alto')
        banco_paga = (valor * 3) / 10
        lista_saida.append(banco_paga)

    return lista_saida

print calcula_seguro(2000.0, [21, True, True, True, True, True, 'Misto'])

