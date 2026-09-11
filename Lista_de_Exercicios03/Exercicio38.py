# Exercício 38 — Evolução salarial. Sarah Gabrielli Rodrigues de Souza Ribeiro - 31/08/2026.
# Pedir o ano final do cálculo (entre 1995 e 2005) e mostrar, ano a ano, o percentual e o salário.
# Cada aumento anual igual ao dobro do percentual do anterior. Inicial 1,5%.

try:
    Salario = float(input("Por gentileza, informe o salário inicial de 1995: "))
    AnoFinal = int(input("Informe o ano final do cálculo (entre 1995 e 2005): "))

    if Salario <= 0:
        print("O salário deve ser maior que zero.")

    elif AnoFinal < 1995 or AnoFinal > 2005: # SELEÇÃO — só é avaliado se a anterior for falsa
        print("Ano inválido! Digite um ano entre 1995 e 2005.")

    else: 
        Percentual = 0

        for Ano in range(1995, AnoFinal + 1): # REPETIÇÃO CONTADA: quando o número de voltas é conhecido

            if Ano == 1996:
                Percentual = 1.5

            elif Ano >= 1997:
                Percentual *= 2

            if Ano > 1995:
                Salario = Salario + (Salario * Percentual / 100)

            print("Ano:", Ano,
                  "| Percentual aplicado:", Percentual, "%",
                  "| Salário:", format(Salario, ".2f"))

except ValueError: # EXCEÇÃO — recusa valores fora dos parâmetro
    print("Valor inválido! Digite os dados corretamente.")

# "O que acontece com o percentual se o cálculo for estendido até o ano atual — e por que essa regra não se sustenta na prática."
# Se essa regra fosse estendida por um laço infinito — ou até mesmo para 2026 — o percentual dobraria MUITO a cada ano.
# Ao seguir com essa ideia, ela iria crescer de forma exponencial, tornando os salários a serem pagos muito economicamente inviáveis.