# Exercício 43 - Lista de Exercícios 03
total = 0
codigo = int(input("Digite o código do produto ou 0 para encerrar: "))
while codigo != 0:
    if codigo < 100 or codigo > 105:
        print("Código inválido!")
    else:
        quantidade = int(input("Digite a quantidade: "))
        while quantidade <= 0:
            print("Quantidade inválida!")
            quantidade = int(input("Digite novamente: "))
        if codigo == 100:
            produto = "Cachorro Quente"
            preco = 10.20
        elif codigo == 101:
            produto = "Bauru Simples"
            preco = 10.30
        elif codigo == 102:
            produto = "Bauru com Ovo"
            preco = 11.50
        elif codigo == 103:
            produto = "Hambúrguer"
            preco = 15.20
        elif codigo == 104:
            produto = "Cheeseburguer"
            preco = 17.30
        else:
            produto = "Refrigerante"
            preco = 10.00
        valor_produto = preco * quantidade
        total = total + valor_produto
        print(f"{produto}: R$ {valor_produto:.2f}")
    codigo = int(input("Digite outro código ou 0 para encerrar: "))
print(f"Total do pedido: R$ {total:.2f}")
