# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Esterias de produção

def distribui_materia_prima(esteira_de_materia_prima, n):
    lista_saida = []
    lista = []
    quantidade_elementos = len(esteira_de_materia_prima) / n
    for i in range(len(esteira_de_materia_prima)):
        if i % quantidade_elementos == 0 and i != 0:
            lista_saida.append(lista)
            lista = []
        lista.append(esteira_de_materia_prima[i])
    
    return lista_saida

esteira_de_materia_prima = ['camera', 'fone', 'microfone', 'processador', 'tela']
print distribui_materia_prima(esteira_de_materia_prima, 3)
        

