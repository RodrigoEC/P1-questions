# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Unidade de medida

def xplit(frase):
    lista = []
    palavra = ""
    for caracter in frase:
        if caracter == " ":
            lista.append(palavra)
            palavra = ""
        if caracter != " ":
            palavra += caracter
        
    lista.append(palavra)
    return lista
    
        
medidas = {"km": 1000, "hm": 100, "dam": 10, "m": 1, "dm": 0.1, "cm":  0.01, "mm":  0.001}
lista_saida = []
while True:
    sentenca = raw_input()
    lista_palavras = xplit(sentenca)
    if lista_palavras[0] == "0" and lista_palavras[2] == "0": break
        
    soma = 0
    for i in range(len(lista_palavras)):
        if i % 2 == 0:
            soma += float(lista_palavras[i]) * medidas[lista_palavras[i + 1]]

    lista_saida.append(soma)

for resultado in lista_saida:
    print "%.2f m" % resultado