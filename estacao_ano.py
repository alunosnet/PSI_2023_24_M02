"""Um programa que lê o nº do dia do ano (1 a 365) e indica a estação do ano

"""
while True:
    dia=int(input("Qual o dia do ano:"))
    if dia>=1 and dia<=365:
        break
#inverno
#[365 a 78]
if dia>=356 or dia<=78:
    print("Inverno")
#Primavera [79 a 171]
elif dia>=79 and dia<=171:
    print("Primavera")
#Verão [172 a 264]
elif dia>=172 and dia<=264:
    print("Verão")
else:
    print("Outono")