# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Resumos iguais

def agrupa_resumos_iguais(lista):
    resumo_dos_numeros = {}
    for numero in lista:
        soma = 0
        for caracter in str(numero):
            soma += int(caracter)
        
        if not resumo_dos_numeros.has_key(soma):
            resumo_dos_numeros[soma] = [numero]
        
        else:
            resumo_dos_numeros[soma].append(numero)
    
    return resumo_dos_numeros