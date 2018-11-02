# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Char Único

def char_unico(frase):
    contador = 0
    saida = ''
    for e in frase:
        for elemento in frase:
            if e == elemento:
                contador += 1
        if contador == 1:
            saida += e
        contador = 0
        
    return saida