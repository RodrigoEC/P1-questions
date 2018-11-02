# coding: utf-8
# Aluno: Rodrigo Eloy Cavalcanti
# Matrícula: 118210111
# E-mail perdido

def encontra_email_perdido(emails_enviados, emails_recebidos):
    for i in range(len(emails_enviados) -1, -1, -1):
        for e in range(len(emails_recebidos) -1, -1, -1):
            if emails_enviados[i] == emails_recebidos[e]:
                emails_enviados.pop(i)
                emails_recebidos.pop(e)
                break

    if len(emails_enviados) > 0:
        return emails_enviados[0]
    if len(emails_recebidos) > 0:
        return emails_recebidos[0]