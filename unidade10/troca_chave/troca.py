# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Troca chave

def troca_chave(dic):
    novo_dicionario = {}
    for (chave, valor) in dic.items():
        novo_dicionario[valor] = chave
    
    return novo_dicionario