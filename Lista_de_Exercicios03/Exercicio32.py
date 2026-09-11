# Exercício 32 - Lista de Exercícios 03
# Leitura e validação da entrada (deve ser um inteiro >= 0)
n = int(input("Fatorial de: "))
while n < 0:
    print("Erro: O fatorial não está definido para números negativos.")
    n = int(input("Fatorial de: "))

# Tratamento do caso especial 0! = 1
if n == 0:
    print("0! = 1")
else:
    fatorial = 1
    termos = []

    # Laço decrescente de n até 1
    for i in range(n, 0, -1):
        fatorial *= i
        termos.append(str(i))

    # Junta os números com ' . ' para montar a expressão por extenso
    expressao = " . ".join(termos)
    print(f"{n}! = {expressao} = {fatorial}")