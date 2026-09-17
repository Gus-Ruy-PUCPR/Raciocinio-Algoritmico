continuar = "n"
list_numbers = []
number, var_0_25, var_26_50, var_51_75, var_76_100 = 0

while True:
    number = float(input("Digite um numero (0 para encerrar a contagem): "))
    if number == 0:
        break
    list_numbers.append(number)
for i in list_numbers:
    if i > 0 and i < 26:
        var_0_25 += 1
    elif i >= 26 and i < 50:
        var_26_50 += 1
    elif i >= 50 and i < 76:
        var_51_75 += 1
    elif i >= 76 and i <= 100:
        var_76_100 += 1
        
print(f"de 0 a 25: {var_0_25}")
print(f"de 26 a 50: {var_26_50}")
print(f"de 51 a 75: {var_51_75}")
print(f"de 76 a 100: {var_76_100}")