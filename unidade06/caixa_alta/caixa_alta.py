# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Caixa Alta

def caixa_alta(frase):
    string = ""
    frase = " " + frase + " "
    for i in range(1, len(frase) - 1):
		if frase[i - 1] == " " and frase[i + 1] == " ":
			string += frase[i].lower()
		elif frase[i - 1] == " " and frase[i + 1] != " ":
			string += frase[i].upper()
		elif frase[i - 1] != " " or frase[i + 1] == " ":
			string += frase[i]
    return string