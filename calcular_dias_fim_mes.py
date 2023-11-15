"""Calcular quantos dias faltam para o fim do mês

Dados: dia e o mês atual
"""


while True:
    mes = int(input("Qual o mês:"))
    #validar o mês
    if mes<1 or mes>12:
        print("O valor do mês deve estar entre 1 e 12")
    else:
        break

while True:
    dia = int(input("Qual o dia:"))
    #meses com 31 dias
    if mes in (1,3,5,7,8,10,12):
        restante = 31 - dia
    elif mes == 2:
        restante = 28 - dia
    else:
        restante = 30 - dia

    #validar o dia
    if restante<0 or dia<1:
        print("O dia indicado não é válido.")
    else:
        break

print(f"Falta {restante} dias para o fim do mês")