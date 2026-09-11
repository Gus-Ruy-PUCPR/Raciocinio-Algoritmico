# Exercício 13 — Potenciação manual
# Nível 2 — Fundamental · Padrão algorítmico: Acumulador multiplicativo
# Faça um programa que peça dois números — base e expoente —, calcule e mostre o primeiro elevado ao segundo.
# Não utilize o operador ** nem a função pow() da linguagem.
# Considere apenas expoentes inteiros maiores ou iguais a zero e valide essa condição.
# Dica: Potenciação é multiplicação repetida. Iniciar o resultado em 1 garante a resposta correta quando o expoente é zero.

# Leitura da base
base = int(input("Digite a base: "))

# Leitura e validação do expoente (deve ser inteiro e >= 0)
expoente = int(input("Digite o expoente (inteiro >= 0): "))

while expoente < 0:
    print("Erro: O expoente deve ser maior ou igual a zero.")
    expoente = int(input("Digite um expoente válido (inteiro >= 0): "))

# Acumulador multiplicativo
resultado = 1

# Multiplicação
for _ in range(expoente):
    resultado *= base

print(f"{base} elevado a {expoente} é igual a: {resultado}")