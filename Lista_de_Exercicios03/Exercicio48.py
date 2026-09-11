#                           Exercício 48 - Thiago Augusto da Silva - 01/09                                          #
#####################################################################################################################
# Faça um programa que peça um número inteiro positivo e em seguida mostre esse número invertido, sem               #
# converter o número em texto.                                                                                      #
#####################################################################################################################

# Criando variáveis para evitar erros depois
num = int(0)
numInv = int(0)
output = str()

while True:
    try:
        num = int(input("Digite um número positivo e inteiro: "))
        if num < 0:
            print("Por favor digite um número positivo!")
        else: break
    except:
        print("Por favor digite um número inteiro!")
numRep = str(num)

for i in range(len(numRep)+1):
    numAtual = num % 10 # Retorna o último digito (123 -> 3)
    num = num // 10 # Remove o último digito do número inserido (123 -> 12)
    if i == len(numRep):
        continue
    elif i == 0 and numAtual == 0: # Exceção para números que terminam em zero (Tal como dez, por exemplo)
        output = "0"
    else:
        numInv *= 10
        numInv += numAtual
output += str(numInv) # Se não fosse uma string não poderia ter a exceção para dezimais exatas
print("O número escolhido foi:", numRep, " E o inverso é: ", output)
