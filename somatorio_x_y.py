#somar todos os números inteiros entre 2 nº indicados pelo utilizador
x=int(input("Nº"))
y=int(input("Nº"))

#trocar os valores se o primeiro for maior que o segundo
if x>y:
    t=x
    x=y
    y=t

if x==y:
    soma =x
else:
    soma=0
    
for i in range(x,y+1):
    soma = soma +i

print(soma)