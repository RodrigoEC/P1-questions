# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# Porta Eletrônica

contador_rb = 0
contador_ra = 0
contador_resto = 0
string_saida = ''
while True:
    entrada = raw_input()
    lista_entrada = entrada.split()
    if lista_entrada[0] == 'S':
        break
    elif lista_entrada[0] == 'R':
        for letra in lista_entrada[1]:
            if letra == 'A':
                contador_ra += 1
                break
            
            elif letra == 'B':
                contador_rb += 1
                break
            else:
                contador_resto += 1

    if lista_entrada[0] == 'P':
        if lista_entrada[1] == 'B':
            string_saida += str(contador_rb)
        elif lista_entrada[1] == 'A':
            string_saida += str(contador_ra)
        else:
            string_saida += str(contador_resto)

for saida in string_saida:
    print saida