# 11. Compra pelo menor preço
# Faça um programa que pergunte o preço de três produtos e informe qual produto deve ser comprado,
# sabendo que a decisão é sempre pelo mais barato. Em caso de empate, indique o produto de menor número
# de ordem.

p1 = float(input("Preço do produto 1: "))
p2 = float(input("Preço do produto 2: "))
p3 = float(input("Preço do produto 3: "))

if p1 <= p2 and p1 <= p3:
    print("Compre o Produto 1!!!")
elif p2 <= p1 and p2 <= p3:
    print("Compre o Produto 2!!!")
else:
    print("Compre o Produto 3!!!")