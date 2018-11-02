# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Analytics votação



def conta_votos(votacoes, idi):
    lista_ids = []
    lista_sn = []
    for frase in votacoes:
        ide = ''
        sim_ou_nao = ''
        contador_virg = 0

        for caracter in frase:
            if caracter == ',':
                contador_virg += 1

            if contador_virg == 1 and caracter != ',':
                ide += caracter

            elif contador_virg == 2 and caracter == ',':
                lista_ids.append(ide)

            elif contador_virg == 4 and caracter != ',':
                sim_ou_nao += caracter
                if sim_ou_nao == 'sim' or sim_ou_nao == 'nao': 
                    lista_sn.append(sim_ou_nao)

    contador_s = 0
    contador_n = 0
    for i in range(len(lista_ids)):
        if lista_ids[i] == str(idi):
            if lista_sn[i] == 'sim':
                contador_s += 1
            elif lista_sn[i] == 'nao':
                contador_n += 1

    saida = [contador_s, contador_n]
    return saida



            