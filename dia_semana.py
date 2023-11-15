"""Calcular e mostrar o dia da semana em que o utilizador nasceu

"""
import datetime

ano=int(input("Ano em que nasceu:"))
mes=int(input("Mês em que nasceu:"))
dia=int(input("Dia em que nasceu:"))

data=datetime.date(ano,mes,dia)

#dia da semana como um número
print(data.weekday())
#dia da semana como texto (inglês)
print(data.strftime("%A"))
