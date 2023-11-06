"""Resolução do exercício 5 do Desafio 1 do módulo 2
    Prof. Paulo Ferreira
    Escola Secundária de Emídio Navarro - Viseu
"""
valor = -1

while valor<0:
    valor = int(input("Introduza um valor inteiro positivo:"))
    if valor<0:
        print("Valor não é válido.")

if valor % 2 == 0:
    print("Valor é par")
else:
    print("Valor é impar")