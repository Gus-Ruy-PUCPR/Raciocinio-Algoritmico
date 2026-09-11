# Exercício 05 — Corrida populacional parametrizada
# Nível 3 — Aplicação · Padrão algorítmico: Validação + laço externo de repetição
# Altere o programa do exercício 4 permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide as entradas (populações maiores que zero e taxas não negativas) e permita repetir a operação quantas
# vezes o usuário desejar.
# ATENÇÃO: antes de iniciar a simulação, verifique se a ultrapassagem é matematicamente possível. Se A já for
# menor que B e a taxa de A for menor ou igual à de B, o laço nunca terminaria; nesse caso, informe que a
# ultrapassagem não ocorrerá.
# Dica: Este é um dos objetivos centrais da lista: reconhecer e evitar laços infinitos.

while True:
    # 1. Leitura e Validação da População A
    pop_a = float(input("Informe a população do País A (> 0): "))
    while pop_a <= 0:
        print("Erro: A população deve ser maior que zero.")
        pop_a = float(input("Informe a população do País A (> 0): "))

    # Leitura e Validação da Taxa A
    taxa_a = float(input("Informe a taxa de crescimento do País A em % (>= 0): "))
    while taxa_a < 0:
        print("Erro: A taxa não pode ser negativa.")
        taxa_a = float(input("Informe a taxa do País A em % (>= 0): "))

    # 2. Leitura e Validação da População B
    pop_b = float(input("Informe a população do País B (> 0): "))
    while pop_b <= 0:
        print("Erro: A população deve ser maior que zero.")
        pop_b = float(input("Informe a população do País B (> 0): "))

    # Leitura e Validação da Taxa B
    taxa_b = float(input("Informe a taxa de crescimento do País B em % (>= 0): "))
    while taxa_b < 0:
        print("Erro: A taxa não pode ser negativa.")
        taxa_b = float(input("Informe a taxa do País B em % (>= 0): "))

    # Conversão das taxas de porcentagem para decimal
    taxa_a_dec = taxa_a / 100
    taxa_b_dec = taxa_b / 100

    # 3. Verificação de Viabilidade Matemática (Evita Laço Infinito)
    if pop_a < pop_b and taxa_a_dec <= taxa_b_dec:
        print("\n[Aviso] A ultrapassagem NUNCA ocorrerá!")
        print("A população de A é menor que B e sua taxa de crescimento é menor ou igual à de B.")
    else:
        anos = 0
        while pop_a < pop_b:
            pop_a += pop_a * taxa_a_dec
            pop_b += pop_b * taxa_b_dec
            anos += 1

        print(f"Resultado da simulação:")
        print(f"- Anos necessários: {anos}")
        print(f"- População final de A: {int(pop_a):,}".replace(",", "."))
        print(f"- População final de B: {int(pop_b):,}".replace(",", "."))

    # 4. Pergunta se o usuário deseja repetir
    opcao = input("\nDeseja realizar outra simulação? (s/n): ").strip().lower()
    if opcao != 's':
        break