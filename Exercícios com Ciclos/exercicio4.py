"""
4.Em Portugal, o sistema de pontos na carta de condução foi implementado para promover uma condução mais segura e responsável. Cada condutor começa com um total de 12 pontos, que podem ser perdidos em função das infrações cometidas. A quantidade de pontos perdidos depende da gravidade da infração.

Infrações muito graves: resultam na perda de 6 pontos. 
Infrações graves: Estas infrações levam à perda de 4 pontos.
Infrações leves: Não perde pontos caso seja a primeira infração deste tipo, ou perde 1 ponto nas restantes vezes.
Duas infrações graves ou uma infração grave e uma muito grave levam à perda da carta durante 1 ano.

O condutor também perde a carta quando fica com 0 (zero) pontos.

Por exemplo:
Tem 12 pontos restantes
Escolha uma opção:
1. Infração muito grave
2. Infração grave
3. Infração leve
4. Terminar

"""
pontos=12
infracao_leve=0
opcao=0
while opcao!=4:
    