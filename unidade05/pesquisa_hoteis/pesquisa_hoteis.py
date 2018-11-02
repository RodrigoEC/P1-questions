# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Pesquisa Hotéis

preco = []
tamanho = []
conforto = []
hoteis = []
while True:
  valores = raw_input()
  if valores == '---': break
  lista_valores = valores.split(',') 

  # Distribuição dos valores nas listas apropriadas
  preco.append(float(lista_valores[0]))
  tamanho.append(float(lista_valores[1]))
  conforto.append(float(lista_valores[2]))
  hoteis.append(lista_valores[3])
while True:
  entrada = raw_input()
  if entrada == 'fim':
    break   

  elif entrada == 'valor':
    menor = preco[0]
    indice = 0
    for i in range(len(preco)):
        if preco[i] < menor:
            menor = preco[i]
            indice = i
    print hoteis[indice]  

  elif entrada == 'tamanho':
    maior = tamanho[0]
    indice = 0
    for i in range(len(tamanho)):
        if tamanho[i] > maior:
            maior = tamanho[i]
            indice = i
    print hoteis[indice]

  elif entrada == 'conforto':
    maior = conforto[0]
    indice = 0
    for i in range(len(conforto)):
        if conforto[i] > maior:
            maior_ = conforto[i]
            indice = i
    print hoteis[indice]