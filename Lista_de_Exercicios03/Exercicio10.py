# Exercício 10 — Intervalo entre dois números
# Nível 2 — Fundamental · Padrão algorítmico: Laço contado com limites variáveis
# Faça um programa que receba dois números inteiros e gere todos os números inteiros do intervalo compreendido
# por eles, incluindo os dois extremos.
# O programa deve funcionar mesmo que o usuário informe os valores em ordem decrescente (por exemplo, 9 e 3).

# Leitura des dois números inteiros
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))

# Define inicio e fim
if a < b:
    inicio = a
    fim = b
else:
    inicio = b
    fim = a

print(f"Numeros no intervalo entre {inicio} e {fim}:")

# Gera o intervalo do menor até o maior
for numero in range(inicio, fim + 1):
    print(numero, end=" ")
print()