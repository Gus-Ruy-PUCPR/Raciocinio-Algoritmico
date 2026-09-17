# Exercício 02 — Senha diferente do usuário
# Nível 1 — Aquecimento · Padrão algorítmico: Validação de entrada
# Faça um programa que leia um nome de usuário e a sua senha. O programa não deve aceitar senha igual ao nome
# do usuário: nesse caso, exiba uma mensagem de erro e volte a pedir as duas informações.

# Loop infinito
while 1:
    login = input("Insira seu Login: ")
    senha = input("Insira sua Senha: ")

    # Se senha for igual a nome pede novamente os dados
    if senha == login:
        print("Seu Login é igual a sua senha!")
    else:
        print("Bem-vindo!")
        break