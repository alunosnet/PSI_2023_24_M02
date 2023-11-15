"""Calcular a idade do utilizador

    Dados: dia, mês e ano de nascimento
"""
import datetime

dia_nasce = int(input("Dia em que nasceu:"))
mes_nasce = int(input("Mês em que nasceu:"))
ano_nasce = int(input("Ano em que nasceu:"))

hoje = datetime.date.today()

ANO_ATUAL = hoje.year
MES_ATUAL = hoje.month
DIA_ATUAL = hoje.day

idade = ANO_ATUAL - ano_nasce

#verificar se ainda não fez anos
if mes_nasce>MES_ATUAL or (mes_nasce==MES_ATUAL and dia_nasce>DIA_ATUAL):
    idade = idade - 1

print(f"Tem {idade} anos.")
