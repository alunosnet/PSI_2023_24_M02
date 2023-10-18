classe = input("Indique a sua classe:")
horas = int(input("Indique as horas que trabalhou:"))

if classe!="1" and classe!="2":
    print("Erro! A classe tem de ser 1 ou 2")
else:
    preco_hora=100
    preco_hora_extra=120
    if classe=="2":
        preco_hora=200
        preco_hora_extra=240
    horas_extra = horas - 40
    if horas_extra<0:
        horas_extra=0
    salario = preco_hora*(horas-horas_extra)+(horas_extra*preco_hora_extra)
    print("Salário a receber %.2f"%salario)