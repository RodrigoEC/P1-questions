# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Labir move direita

def move_direita(labirinto):
    for linha in range(len(labirinto)):
        for elemento in range(len(labirinto[linha])):
            if labirinto[linha][elemento] == '*':

                if elemento == len(labirinto[linha]) - 1:
                    return (linha, elemento)

                elif labirinto[linha][elemento + 1] == 'P':
                    return (linha, elemento)

                elif labirinto[linha][elemento + 1] == ' ':
                    labirinto[linha][elemento], labirinto[linha][elemento + 1] \
                     = labirinto[linha][elemento + 1], labirinto[linha][elemento]
                    return (linha, elemento + 1)