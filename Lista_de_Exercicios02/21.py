# 21. Classificação de triângulos
# Faça um programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem
# formar um triângulo e, em caso afirmativo, se ele é equilátero, isósceles ou escaleno.
# • Os lados devem ser valores positivos.
# • Três lados formam um triângulo quando a soma de quaisquer dois deles é maior que o terceiro.
# • Triângulo equilátero: três lados iguais. Isósceles: exatamente dois lados iguais. Escaleno: três lados
# diferentes.

lado_a = int(input("Digite o primeiro lado: "))
lado_b = int(input("Digite o segundo lado: "))
lado_c = int(input("Digite o terceiro lado: "))

a = int(lado_a)
b = int(lado_b)
c = int(lado_c)

if a <= 0 or b <= 0 or c <= 0:
    print("Erro: Os lados devem ser valores positivos maiores que zero.")
elif not (a + b > c and a + c > b and b + c > a):
    print("Os valores informados não formam um triângulo.")
elif a == b == c:
    print("O triângulo é EQUILÁTERO.")
elif a == b or b == c or a == c:
    print("O triângulo é ISÓSCELES.")
else:
    print("O triângulo é ESCALENO.")