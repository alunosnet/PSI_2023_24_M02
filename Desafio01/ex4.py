"""Resolução do exercício 4 do Desafio 1 do módulo 2
    Prof. Paulo Ferreira
    Escola Secundária de Emídio Navarro - Viseu
"""
contar=0
for i in range(10):
    letra=input("Escreva uma letra:")
    if letra in "aeiouAEIOU":
        contar = contar + 1

print("Escreve %d vogais"%contar)