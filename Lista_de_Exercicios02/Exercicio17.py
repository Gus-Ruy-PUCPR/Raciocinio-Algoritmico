# 17. Folha de pagamento
# Faça um programa para o cálculo de uma folha de pagamento. O programa deve pedir ao usuário o valor da
# hora trabalhada e a quantidade de horas trabalhadas no mês, e a partir disso calcular o salário bruto. Sobre
# o salário bruto incidem dois descontos: o Imposto de Renda, cuja alíquota depende da faixa do salário bruto
# (tabela abaixo), e a contribuição sindical, fixada em 3%. O FGTS corresponde a 11% do salário bruto, mas não
# é descontado — é depositado pela empresa e aparece no demonstrativo apenas como informação. O salário
# líquido corresponde ao salário bruto menos os descontos.
# Salário bruto Desconto de IR
# até R$ 900,00 (inclusive) isento
# acima de R$ 900,00 até R$ 1.500,00 (inclusive) 5%
# acima de R$ 1.500,00 até R$ 2.500,00 (inclusive) 10%
# acima de R$ 2.500,00 20%
# Imprima na tela as informações dispostas conforme o exemplo abaixo, no qual o valor da hora é 5,00 e a
# quantidade de horas é 220.
# Salário bruto (5.00 x 220) : R$ 1100.00
# (-) IR (5%) : R$ 55.00
# (-) Sindicato (3%) : R$ 33.00
# FGTS (11%) : R$ 121.00
# Total de descontos : R$ 88.00
# Salário líquido : R$ 1012.00

valor_hora = float(input("Qual o valor da hora trabalhada: "))
horas_trabalhadas = float(input("Quantidade de horas trabalhadas: "))

salario_bruto = valor_hora * horas_trabalhadas
c_sindical = salario_bruto*3/100

if salario_bruto < 0 or horas_trabalhadas < 0:
    print("Valores inválidos!!!")
    exit()

if salario_bruto <= 900:
    ir = "(00%)"
    calculo_ir = salario_bruto*0/100
elif salario_bruto <= 1500:
    ir = "(05%)"
    calculo_ir = salario_bruto*5/100
elif salario_bruto <= 2500:
    ir = "(10%)"
    calculo_ir = salario_bruto*10/100
elif salario_bruto > 2500:
    ir = "(20%)"
    calculo_ir = salario_bruto*20/100

fgts = salario_bruto*11/100
salario_liquido = salario_bruto - calculo_ir - c_sindical

print(f"Salário Bruto:          {salario_bruto} ({valor_hora} X {horas_trabalhadas})")
print(f"Imposto de Renda {ir}: {calculo_ir}")
print(f"Sindicato (3%):         {c_sindical}")
print(f"FGTS (11%):             {fgts}")
print(f"Total de deduções:      {calculo_ir + c_sindical}")
print(f"Salário Líquido:        {salario_liquido}")