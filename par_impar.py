#programa para indicar se um nº é par ou impar
numero = int(input("Nº a verificar:"))

resto = numero % 2

if resto == 0:
    print("Nº é par")
else:
    print("Nº é impar")
