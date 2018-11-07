# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Mastery Learning

print 'Mastery Learning'
print 'Cálculo da nota na unidade'
print

nota1 = float(raw_input('Nota? '))
nota2 = float(raw_input('Nota? '))
media = (nota1 + nota2) / 2
if media >= 6:
    print 'Média: %.1f (aprovado)' % media
    print 'Penalização: 0.0'
    print
else:
    print 'Média: %.1f (cursando)' % media
    print 'Penalização: 0.0'
    print

penalizacao = 0
notas_validas = '%.1f e %.1f' % (nota1, nota2)
while media < 6:
    nota = float(raw_input('Nota? '))
    penalizacao += 0.5

    if nota > nota1 and nota1 > nota2:
        nota2 = nota1
        nota1 = nota
        media = (nota2 + nota) / 2
        notas_validas = str(nota) + ' e ' + str(nota2)

    elif nota > nota1 and nota2 > nota1:
        nota1 = nota2
        nota2 = nota
        media = (nota1 + nota) / 2
        notas_validas = str(nota) + ' e ' + str(nota1)
    if media >= 6:
        print 'Média: %.1f (aprovado)' % media
        print 'Penalização: %.1f' % penalizacao
        print
    else:
        print 'Média: %.1f (cursando)' % media
        print 'Penalização: %.1f' % penalizacao
        print

media_final = media - penalizacao
print '==='
print 'Notas válidas: %s' % notas_validas
print 'Média parcial na unidade: %.1f' % media
print 'Penalizações: %.1f' % penalizacao
print 'Média final na unidade: %.1f' % media_final
        
