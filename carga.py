"""
    Programa para controlar a carga de um camião
    O camião pode carregar no máximo 10000Kg
    Menu: 1- Carregar; 2- Descarregar; 3- Sair
"""
peso_atual = 0
while True:
    print(f"Peso atual: {peso_atual} Disponibilidade: {10000-peso_atual}")
    print("1. Carregar\n2. Descarregar\n3. Sair\n")
    opcao = input("Escolha uma opção:")
    #se escolher sair
    if opcao=="3":
        break
    #se escolher carregar
    if opcao=="1":
        #qual o peso da carga
        peso = int(input("Qual o peso a carregar?"))
        if peso<0:
            print("Valor inválido")
            continue
        peso_atual = peso_atual + peso
        if peso_atual > 10000:
            print("Peso máximo excedido.")
            peso_atual = peso_atual - peso
    #se escolher descarregar
    if opcao=="2":
        peso = int(input("Qual o peso a retirar?"))
        if peso<0:
            print("Valor inválido")
            continue
        peso_atual = peso_atual - peso
        if peso_atual < 0:
            print("Valor de carga não existe.")
            peso_atual = peso_atual + peso
