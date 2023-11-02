frase=input("Frase:")
for i in range(len(frase)):
    if frase[i].isalpha():
        print("Alfanumérico")
    if frase[i].isdigit():
        print("Digito")
    if frase[i].isspace():
        print("Espaço")