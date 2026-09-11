#                           Exercício 49 - Thiago Augusto da Silva - 31/08                                          #
#####################################################################################################################
# Faça um programa que mostre os n primeiros termos da série S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m e imprima, #
# ao final, a soma da série.                                                                                        #
# Observe a regra de formação: o numerador avança de 1 em 1 e o denominador percorre os números ímpares.            #
#####################################################################################################################

resultadoFinal = float(1.0)

try:
    numRep = int(input("Digite um valor inteiro e positivo: "))
except:
    print("Tente novamente com um número inteiro, e positivo")
for i in range(1, numRep):
    if i == 1:
        pass
    else:
        resultadoFinal += i / (2*i - 1)
print("O resultado final foi: ", resultadoFinal)