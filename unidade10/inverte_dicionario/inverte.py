# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Inverte dicionario

def inverte_dicionario(d):
    dicionario = {}

    for (key, valor) in d.items():
        if type(valor) == list:
            for v in valor:
                if dicionario.has_key(v):
                    dicionario[v].append(key)
            
                else:

                    dicionario[v] = [key]

        else:
            if dicionario.has_key(valor):
                dicionario[valor].append(key)
            
            else:

                dicionario[valor] = [key]

    return dicionario

m = {"c": 0 , "b": 0}

print inverte_dicionario(m)