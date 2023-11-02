from string import punctuation

nome=input("Nome: ")

for letra in nome:
    print(nome.index(letra)," ",letra,":",end=" ")
    if letra.isalpha():
        print("Alfanumérico",end=" ")
    if letra.isdigit():
        print("Numérico",end=" ")
    if letra.isspace():
        print("Espaço",end=" ")
    if letra in punctuation:
        print("Pontuação",end=" ")
    print(ord(letra))