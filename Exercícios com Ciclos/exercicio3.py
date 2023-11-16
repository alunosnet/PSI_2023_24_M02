"""
3. Você está fazendo compras em um supermercado com um orçamento e uma capacidade de peso limitados. Seu objetivo é maximizar o número de itens que você pode comprar sem exceder seu orçamento e a capacidade de peso que você pode levar.
De cada vez que adicionar um produto à lista de compras deve indicar quanto dinheiro ainda sobre e quanto peso ainda pode carregar.
"""
PesoMax=float(input("Qual o peso máximo:"))
CustoMax=float(input("Quanto dinheiro tem para gastar:"))

PesoTotal=0
CustoTotal=0

while True:
    peso=float(input("Quanto pesa o produto:"))
    if PesoTotal+peso>PesoMax:
        print("Peso excessivo")
        continue
    custo=float(input("Quanto custa o produto:"))
    if CustoTotal+custo>CustoMax:
        print("Custo excessivo")
        continue
    PesoTotal += peso
    CustoTotal += custo
    print(f"Já gastou {CustoTotal} e as suas compras pesam {PesoTotal}")
    continuar=input("Pretende continuar?")
    if continuar!="s" and continuar!="S":
        break