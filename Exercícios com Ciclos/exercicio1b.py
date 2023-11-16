"""
Um programa para calcular a duração total de um album. Para isso é necessário inserir a duração de cada música. A duração de cada música é inserida em segundos, mas a duração total deve ser mostrada em minutos:segundos
b) Ler até inserir duração 0 (zero)
"""

duracao_total=0
while True:
    duracao=int(input("Duração da música em segundos:"))
    #se a duracao é 0 termina o ciclo
    if duracao==0:
        break
    duracao_total += duracao

#converter para minutos
duracao_minutos=int(duracao_total/60)
duracao_segundos=duracao_total-duracao_minutos*60

print(f"A duração total do album {duracao_minutos}:{duracao_segundos}")