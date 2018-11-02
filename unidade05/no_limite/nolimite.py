# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# No limite


lista_numeros = []
while True:
    numero = raw_input()
    if numero == '-':
        break
    lista_numeros.append(numero)

limite = float(raw_input())
contador = 0
soma = 0
for i in range(len(lista_numeros)):
    contador += 1
    soma += float(lista_numeros[i])
    media = float(soma) / contador
    if media > limite:
        print 'media = %.1f' % media
        print 'num = %i' % contador
        break

if media <= limite:
    print 'limite não alcançado'

    
    

