# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Analytics Assembleia

def conta_votos(votacoes, id_votacao):
    lista_ids = []
    lista_sn = []
    for frase in votacoes:
        contador = 0
        sim_nao = ''
        ide = ''
        for caracter in frase:
            if caracter == ',':
                contador += 1

            if contador == 1 and caracter != ',':
                sim_nao += caracter
                
                if sim_nao == 'sim' or sim_nao == 'nao':
                    lista_sn.append(sim_nao)

            elif contador == 2 and caracter != ',':  
                ide += caracter
            elif contador == 3 and caracter == ',':
                lista_ids.append(ide)

    contador_n = 0
    contador_s = 0
    for i in range(len(lista_ids)):
        if lista_ids[i] == str(id_votacao) and lista_sn[i] == 'sim':
            contador_s += 1
        elif lista_ids[i] == str(id_votacao) and lista_sn[i] == 'nao':
            contador_n += 1
    
    saida = [contador_s, contador_n]
    return saida