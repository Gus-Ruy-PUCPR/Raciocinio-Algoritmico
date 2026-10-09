# 3 – Soma de três argumentos


a = 0
b = 0
c = 0

def somar_tres_numeros(a:int, b:int, c:int) -> int:
    return a + b + c

try:
    a = int(input("Digite um numero A: "))
    b = int(input("Digite um numero B: "))
    c = int(input("Digite um numero C: "))
    print(f"A soma dos números {a}, {b} e {c} é: {somar_tres_numeros(a, b, c)}")
except NameError:
    print(NameError)


