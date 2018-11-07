# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Quantidade de usuários

def quantidade_usuarios(cadastro):
    acumulador = 0
    for (key, nomes) in cadastro.items():
        if key != 9999:
            acumulador += len(nomes)
    
    return acumulador