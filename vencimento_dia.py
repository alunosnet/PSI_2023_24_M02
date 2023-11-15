"""Programa para calcular o vencimento de um trabalhador
com base nas datas em que começou e terminou de trabalhar  
e o vencimento por dia

"""
import datetime

#pedir ao utilizador a data em que começou a trabalhar
data_comecou=input("Data em que começou o trabalho:")
#pedir ao utilizador a data em que terminou de trabalhar
data_conclusao=input("Data em que terminou o trabalho:")
#calcular quantos dias trabalhou
data_comecou_obj=datetime.datetime.strptime(data_comecou,"%Y-%m-%d")
data_conclusao_obj=datetime.datetime.strptime(data_conclusao,"%Y-%m-%d")
#calcular a diferença entre a data de conclusão e a data de inicio
dias = data_conclusao_obj-data_comecou_obj
if dias.days<0:
    print("As datas não são válidas!")
else:
    #pedir ao utilizador quanto ganha por dia
    vencimento_dia=float(input("Quanto ganha por dia:"))
    #calcular o vencimento
    vencimento = dias.days * vencimento_dia
    print(f"Deve receber {vencimento}€ porque trabalho {dias.days} dias")
