# Exercício 10 — Intercalação de duas listas. Sarah Gabrielli Rodrigues de Souza Ribeiro - 07/09/2026.
# Ler duas listas de 10. Gerar uma terceira lista, de 20. Seus valores compostos pelos elementos intercalados das duas listas originais, na ordem A[0], B[0], A[1], B[1]...
# Mostrar as três listas no final.

ListaA = []
ListaB = []
ListaC = []

for i in range(10):
    Num = int(input("Por gentileza, digite os valores iniciais: "))
    ListaA.append(Num)

for i in range(10):
    Num = int(input("Por gentileza, digite os valores finais: "))
    ListaB.append(Num)

for i in range(10):
    ListaC.append(ListaA[i])
    ListaC.append(ListaB[i])

print("Lista A:", ListaA)
print("Lista B:", ListaB)
print("Lista C:", ListaC)

# Exercício 10 - FIM.