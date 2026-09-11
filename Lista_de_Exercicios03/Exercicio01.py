# Exercício 01 — Nota válida
# Nível 1 — Aquecimento · Padrão algorítmico: Validação de entrada
# Faça um programa que peça uma nota entre zero e dez. Enquanto o valor informado estiver fora dessa faixa, o
# programa deve exibir uma mensagem de erro e pedir a nota novamente. Ao final, exiba a nota aceita.
# Considere válidos os extremos (0 e 10).

nota = int(-1)
while nota < 0 or nota >10:
    nota = int(input("Digite um numero entre 0 e 10: "))
print("Numero digitado entre 0 e 10!")