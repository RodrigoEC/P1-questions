# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
#coding: utf-8


def num_creditos(bd_ufcg, matricula):
    s_creditos = 0
    for dicionario in bd_ufcg.values():
        for (tupla, matriculas) in dicionario.items():
            for m in matriculas:
                if m == matricula:
                    s_creditos += tupla[1]
    
    return s_creditos





bd_ufcg = {"UASC": {("Programação I", 4): ["11624100", "11624400"], ("Programação II", 4): ["11624200"], ("Teoria dos Grafos", 2): ["11624200"]},
           "UAF": {("Física Clássica", 4): ["11624200"], ("Física Moderna", 4): ["11624300", "11624500", "11624600"]},
           "UAM": {("Cálculo I", 4): ["11624100", "11624300"], ("Álgebra Linear", 4): ["11624300"]}
           }

print num_creditos(bd_ufcg, "11624100")