# 16. Reajuste salarial — Organizações Tabajara
# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e contrataram você
# para desenvolver o programa que calculará os reajustes. Faça um programa que receba o salário atual de um
# colaborador e o reajuste segundo o critério abaixo:
# Faixa do salário atual Aumento
# até R$ 280,00 (inclusive) 20%
# acima de R$ 280,00 até R$ 700,00 (inclusive) 15%
# acima de R$ 700,00 até R$ 1.500,00 (inclusive) 10%
# acima de R$ 1.500,00 5%
# Após o aumento ser realizado, informe na tela o salário antes do reajuste, o percentual de aumento aplicado,
# o valor do aumento e o novo salário após o aumento.

salario = float(input("Digite o valor do seu salário: "))

if salario <= 280:
    almento = salario*20/100
elif salario <= 700:
    almento = salario*15/100
elif salario <= 1500:
    almento = salario*10/100
else:
    almento = salario*5/100

print(f"Salário antes do reajuste: {salario}")
print(f"Salário depois do reajuste: {salario + almento}")
print(f"Almento aplicado: {almento}")