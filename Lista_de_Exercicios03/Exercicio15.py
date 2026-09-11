# Exercício 15 — Fibonacci: n primeiros termos
# Nível 3 — Aplicação · Padrão algorítmico: Geração de série
# A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... na qual cada termo, a partir do
# terceiro, é a soma dos dois anteriores. Faça um programa capaz de gerar a série até o n-ésimo termo, sendo n
# informado e validado pelo usuário.
# Observação: nesta lista adotamos a convenção F1 = 1 e F2 = 1. Existe também a convenção que inicia em 0; o
# importante é ser coerente dentro do mesmo programa.
# Dica: Você precisa de apenas duas variáveis de memória (o termo anterior e o atual) — não use listas.

# Validação da entrada: n deve ser um número inteiro positivo (>= 1)
num = int(input("Informe a quantidade de termos da série (n >= 1): "))
while num < 1:
    print("Erro: A quantidade de termos deve ser maior ou igual a 1.")
    num = int(input("Informe a quantidade de termos da série (n >= 1): "))

# Inicialização dos dois primeiros termos (F1 = 1 e F2 = 1)
a, b = 1, 1

print(f"\nSérie de Fibonacci até o {num}º termo:")

# Trata a exibição baseada na quantidade de termos solicitada
for i in range(1, num + 1):
    if i == 1:
        print(a, end=" ")
    elif i == 2:
        print(b, end=" ")
    else:
        # Calcula o próximo termo e atualiza os valores anteriores
        proximo = a + b
        print(proximo, end=" ")
        a = b
        b = proximo