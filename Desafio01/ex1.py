"""Resolução do exercício 1 do Desafio 1 do módulo 2
    Prof. Paulo Ferreira
    Escola Secundária de Emídio Navarro - Viseu
"""
print("Insira 5 números")
contar=0
while contar<5:
    n=int(input("Insira um número:"))
    if n>10 and n<100:
        contar = contar +1
    print(contar)