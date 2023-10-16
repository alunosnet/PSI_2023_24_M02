dias=int(input("Quantos dias durou o aluguer:"))
kms=int(input("Quantos km foram percorridos:"))
if (dias<1):
    dias=1  #tem de pagar pelo menos um dia

#preço sem iva
preco_sem_iva=dias*10 + kms*0.6

#preço com iva
preco_com_iva=preco_sem_iva + preco_sem_iva*0.23

print("Tem de pagar %.2f"%preco_com_iva)
      