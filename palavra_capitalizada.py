frase = input("Frase:")
frase = frase.strip()
frase2 = frase[0].capitalize()
for i in range(len(frase)-1):
    if frase[i+1]==" ":
        frase2 = frase2 + frase[i+1].upper()
    else:
        frase2 = frase2 + frase[i+1].lower()
print(frase2)