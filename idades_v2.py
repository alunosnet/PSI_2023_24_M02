dados = input("Introduza a sua idade (0 a 120)")

if dados.isdigit()==False:
    print("Tem de introduzir a sua idade com valores numéricos")
else:
    idade = int(dados)
    if idade<0 or idade>120:
        print("A idade não é válida. Tem de estar entre 0 e 120")
    elif idade <=11:
        print("Infância")
    elif idade <=20:
        print("Adolescência")
    elif idade <=74:
        print("Adulto")
    else:
        print("Velhice")
