# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Inverte dicionario
    
def ordem(lista):
	for i in range(len(lista)-1, 0, -1):
		if lista[i] < lista[i-1]:
			lista[i-1], lista[i] = lista[i], lista[i-1]
		else:
			break

def meu_in(dic, ele):
	for chave in dic.keys():
		if chave == ele:
			return True
	return False

def inverte_dicionario(dic):
	cache = {}
	for chave, valor in dic.iteritems():
		if meu_in(cache, valor):
			cache[valor].append(chave)
			ordem(cache[valor])

		else:
			cache[valor] = [chave]

	return cache