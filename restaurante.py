"""
Precisamos de um programa para gerir a lotação de um restaurante
que tem 100 lugares
De cada vez que chegam clientes é introduzido o nº de pessoas a sentar
Se esse nº for 0 (Zero) o programa termina
Se nº for >0 devemos indicar quantos lugares sobram, depois dessas pessoas se sentarem ou se já não há lugares para eles
Hacker:
    Ter em conta que o restaurante só tem 20 mesas, e que de cada vez que entram clientes é ocupada uma mesa
"""
n_lugares=100
mesas = 20
#ciclo infinito
while True:
    #ler quantas pessoas querem entrar
    n_pessoas=int(input("Quantas pessoas para entrar:"))
    #testar se devemos terminar o programa
    if n_pessoas==0:
        break
    #testar se temos lugares disponíveis
    if n_lugares>=n_pessoas and mesas>0:
        #atualizar o nº de lugares livres
        n_lugares = n_lugares - n_pessoas
        #diminuir nº de mesas
        mesas = mesas - 1
        print("Tem ",n_lugares," livres e ",mesas," mesas")
    else:
        print("Não tem tantos lugares livres. Só tem ",n_lugares," e ",mesas," mesas")