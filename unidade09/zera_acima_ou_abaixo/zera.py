# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Zera acima ou abaixo

def zera_acima_ou_abaixo(matriz):
    soma_acima = 0
    soma_abaixo = 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            
            if coluna > linha:
                soma_acima += matriz[linha][coluna]
            
            elif coluna < linha:
                soma_abaixo += matriz[linha][coluna]
        
    
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):

            if soma_abaixo > soma_acima:

                if coluna < linha:
                    matriz[linha][coluna] = 0
            
            elif soma_acima > soma_abaixo:

                if coluna > linha:
                    matriz[linha][coluna] = 0
            
            else:

                if coluna != linha:
                    matriz[linha][coluna] = 0