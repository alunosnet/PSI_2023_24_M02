"""
Validar uma password, indicando se é fraca, média ou forte
"""
palavra_passe=input("Indique a sua senha:")
avaliacao_numeros=0
avaliacao_minusculas=0
avaliacao_maiusculas=0
avaliacao_especiais=0
#se a senha tiver menos de 7 carateres é fraca
if len(palavra_passe)<7:
    print("Fraca")
else:
    for letra in palavra_passe:
        #se tem números
        if avaliacao_numeros==0 and letra in "0123456789":
            avaliacao_numeros=1
        #especiais
        if letra in "#&$£@%!?;:.-_=+*<>\\/^~{}()[]":
            avaliacao_especiais=1
        #minusculas
        if ord(letra)>=97 and ord(letra)<=122:
            avaliacao_minusculas=1
        #maiusculas
        if ord(letra)>=65 and ord(letra)<=90:
            avaliacao_maiusculas=1
        if avaliacao_numeros==1 and avaliacao_minusculas==1 and avaliacao_maiusculas==1 and avaliacao_especiais==1:
            break
    avaliacao=avaliacao_minusculas+avaliacao_maiusculas+avaliacao_especiais+avaliacao_numeros
    #senha fraca
    if avaliacao==1:
        print("Fraca")
    elif avaliacao<=3:
        print("Média")
    else:
        print("Forte")