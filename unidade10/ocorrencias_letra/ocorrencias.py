# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Ocorrencias letra

frase = raw_input()
letra_mais_ocorrente = ""
maior = 0
for letra in frase:
    contador = 0
    for caracter in frase:
        if letra.lower() == caracter.lower() and letra != " ":
            contador += 1

    if contador > maior:
        maior = contador
        letra_mais_ocorrente = letra

print letra_mais_ocorrente.lower(), maior