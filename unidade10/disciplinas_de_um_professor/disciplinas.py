# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Disciplina de um professor



def my_in(lista, elemento):
    for e in lista:
        if elemento == e:
            return True
    
    return False

def contador_professor(lista, elemento):
    contador = 0
    for e in lista:
        if elemento == e:
            contador += 1

    return contador

def disciplinas(alocacao, professor):
    lista_alocacoes = []
    creditos = 0
    for (tupla, professores) in alocacao.items():

        if my_in(professores, professor):
            lista_alocacoes.append(tupla[0])
            creditos += tupla[1] * contador_professor(professores,professor)

    for i in range(len(lista_alocacoes) -1):
        for i in range(len(lista_alocacoes) - 1):

            if lista_alocacoes[i] < lista_alocacoes[i - 1]:
                lista_alocacoes.append(lista_alocacoes.pop(i))
                break

    return (lista_alocacoes, creditos)