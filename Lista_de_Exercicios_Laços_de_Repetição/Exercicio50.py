#                           Exercício 50 - Thiago Augusto da Silva - 31/08                                          #
#####################################################################################################################
# Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que calcule o valor de H com N termos.                #
# Exiba o resultado com pelo menos seis casas decimais e observe como a soma cresce muito lentamente à medida       #
# que N aumenta.                                                                                                    #
#####################################################################################################################

resultadoFinal = float(1)

try:
    numRep = int(input("Digite um valor inteiro e positivo: "))
except:
    print("Tente novamente com um número inteiro, e positivo")
for i in range(2, (numRep+1)):
    resultadoFinal += 1 / i
print("O resultado final é: %.6f" % resultadoFinal)