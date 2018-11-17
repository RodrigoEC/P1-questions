# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Livros estoque

def ausentes(estoque):
    contador = 0
    for valor in estoque.values():
        if valor == 0:
            contador += 1
    
    return contador