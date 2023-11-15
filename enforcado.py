"""Jogo do enforcado V0.5

"""
palavra="banana"
palavra_j="_"*len(palavra)
tentativas=7
while tentativas>0:
    letra=input("Letra:").lower()
    temp=""
    acertou = False
    for i in range(len(palavra)):
        if letra==palavra[i]:
            temp += letra
            acertou = True
        else:
            temp += palavra_j[i]
    palavra_j=temp
    #testar se não acertou na letra
    if acertou==False:
        tentativas -= 1
    #testar se ganhou
    if palavra==palavra_j:
        print(f"Acertou na palavra: {palavra}")
        break
    print(palavra_j)
    print(f"Tentativas restantes {tentativas}")
if tentativas==0:
    print(f"Errou a palavra. A palavra era {palavra}")
