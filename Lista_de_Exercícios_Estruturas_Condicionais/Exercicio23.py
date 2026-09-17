# 23. Calculadora com classificação do resultado
# Faça um programa que leia dois números e em seguida pergunte ao usuário qual operação ele deseja realizar
# (+, -, * ou /). O programa deve rejeitar operadores inválidos e a divisão por zero. O resultado da operação
# deve ser acompanhado de frases que digam se o resultado é:
# • positivo, negativo ou nulo;
# • inteiro ou decimal;
# • par ou ímpar — classificação que só se aplica quando o resultado for inteiro.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+, -, *, /): ").strip()

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 == 0:
        print("Erro: Divisão por zero não é permitida.")
        resultado = None
    else:
        resultado = num1 / num2
else:
    print("Erro: Operador inválido.")
    resultado = None

if resultado is not None:
    print(f"Resultado da operação: {resultado:.2f}")
    
    if resultado > 0:
        print("- O resultado é: POSITIVO")
    elif resultado < 0:
        print("- O resultado é: NEGATIVO")
    else:
        print("- O resultado é: NULO")
        
    if resultado == int(resultado):
        print("- O resultado é: INTEIRO")

        valor_inteiro = int(resultado)
        if valor_inteiro % 2 == 0:
            print("- O resultado é: PAR")
        else:
            print("- O resultado é: ÍMPAR")
    else:
        print("- O resultado é: DECIMAL")