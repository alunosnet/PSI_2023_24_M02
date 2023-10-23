texto = "Enzo a falar com Frederico"
contar_vogais = 0
for letra in texto:
    if letra in "aeiouAEIOU":
        #contar_vogais = contar_vogais + 1
        contar_vogais+=1

print("Tem %d vogais"%contar_vogais)