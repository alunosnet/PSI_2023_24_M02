import random

numero_secreto=int(random.random()*10+1)

while True:
    tentativas = int(input("Nº de tentativas (1 a 5):"))
    if tentativas<1 or tentativas>5:
        print("Nº inválido. Introduza um nº de 1 a 5")
    else:
        break

while tentativas>0:
    print("Tem %d tentativas"%tentativas)
    numero = int(input("Introduza um valor (1 a 10):"))
    if numero>10 or numero<0:
        print("O nº é inválido")
        continue
    #testar se acertou
    if numero == numero_secreto:
        print("Acertou")
        break
    if tentativas>1:
        if numero_secreto > numero:
            print("O nº secreto é superior")
        else:
            print("O nº secreto é menor")
    tentativas = tentativas - 1
else:
    print("O nº secreto era %d"%numero_secreto)