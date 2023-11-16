"""
2. Série de Fibonacci até N: Escreva um programa que imprime a série de Fibonacci até um número N fornecido pelo usuário. Lembre-se de que a série de Fibonacci é uma sequência onde cada número é a soma dos dois anteriores, começando com 0 e 1.
"""

N=int(input("Quantos nº pretende?"))
print("0\n1")
anterior1=0
anterior2=1
for i in range(N-2):
    numero = anterior1+anterior2
    print(numero)
    anterior1=anterior2
    anterior2=numero