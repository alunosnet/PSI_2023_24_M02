#Exitem 3 candidatos a uma eleição
#Devemos calcular a % de votos de cada candidato
#Indicar qual foi o vencedor e se ganhou com maioria absoluta
v1=int(input("Votos candidato 1:"))
v2=int(input("Votos candidato 2:"))
v3=int(input("Votos candidato 3:"))

total = v1+v2+v3

#percentagens de votos por candidato
pv1 = v1/total * 100
pv2 = v2/total * 100
pv3 = v3/total * 100
print(pv1,pv2,pv3)

#maioria absoluta
if pv1>50 or pv2>50 or pv3>50:
    print("Com maioria absoluta")
else:
    print("Sem maioria absoluta")