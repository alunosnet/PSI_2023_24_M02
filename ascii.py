#tabela ASCII
letra = input("Letra do alfabeto:")
ascii_code = ord(letra)
print(ascii_code)

#Carater correspondente ao código ASCII
for i in range(255):
    print(chr(i))