# Exercício 06 — Contagem de 1 a 20
# Nível 1 — Aquecimento · Padrão algorítmico: Laço contado (for)
# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Em seguida, no mesmo
# programa, imprima novamente os mesmos números, agora um ao lado do outro.
# Dica: Para imprimir na mesma linha, use o parâmetro end do print: print(numero, end=" ").

# Loop de 1 a 20, um abaixo do outro 
for i in range(1,21):
    print(i)
# Loop de 1 a 20, um ao lado do outro
for i in range(1,21):
    print(i, end=" ")