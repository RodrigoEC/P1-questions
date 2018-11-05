# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# É quadrado perfeito?

def eh_quadrado_magico(matriz):
    if len(matriz) == 0:
        return False
    comparador = 0
    for i in range(len(matriz[0])):
        comparador += matriz[0][i]
    
    soma_linha = 0
    soma_diag = 0
    soma_diag_oposta = 0
    for linha in range(len(matriz)):
        soma_diag += matriz[linha][linha]
        for numero in range(len(matriz[linha])):            
            soma_linha += matriz[linha][numero]

            if numero + linha == len(matriz) - 1:
                soma_diag_oposta += matriz[linha][numero]

        if soma_linha != comparador:
            return False
        else:
            soma_linha = 0
            
    if soma_diag != comparador or soma_diag_oposta != comparador:
        return False
    soma_diag = 0
    
    soma_coluna = 0
    for numero in range(len(matriz[0])):
        for linha in range(len(matriz)):
            soma_coluna += matriz[linha][numero]
        if soma_coluna != comparador:
            return False
        else:
            soma_coluna = 0
    
    lista_maior = []
    for x in matriz:
        lista_maior += x
    contador = 0
    for x in lista_maior:
        for v in lista_maior:
            if x == v:
                contador += 1
            if contador == 2:
                return False
        contador = 0
    
    return True
        
            
    
    







quadrado1 = [[11,24,7,20,3],[4,12,25,8,16],[17,5,13,21,9],[10,18,1,14,22],[23,6,19,2,15]]
print eh_quadrado_magico(quadrado1)
