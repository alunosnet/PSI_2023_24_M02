base = int(input("Qual a base:"))
expoente = int(input("Qual o expoente:"))
multiplicacao=1
for i in range(expoente):
    multiplicacao = multiplicacao * base
print(multiplicacao)