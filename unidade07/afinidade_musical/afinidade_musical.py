# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Afinidade Musical

def tem_afinidade(playlist1, playlist2):
    contador = 0
    for artista in playlist1:
        for artist in playlist2:
            if artista == artist:
                contador += 1

    if contador >= 3:
        return True

    else:
        return False