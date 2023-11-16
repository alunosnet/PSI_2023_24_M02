"""
Um programa para calcular a duração total de um album. Para isso é necessário inserir a duração de cada música. A duração de cada música é inserida em segundos, mas a duração total deve ser mostrada em minutos:segundos
a) Pedir quantas músicas primeiro

"""

num_musicas = int(input("Quantas músicas:"))
duracao_total=0
for i in range(num_musicas):
    duracao=int(input("Duração da música em segundos:"))
    duracao_total += duracao

#converter para minutos
duracao_minutos=int(duracao_total/60)
duracao_segundos=duracao_total-duracao_minutos*60

print(f"A duração total do album {duracao_minutos}:{duracao_segundos}")