# 10 – Jogo de Craps

import random

def jogar_dados():
    x = random.randint(1,6) + random.randint(1,6)
    return x

def jogar_craps():
    ponto = 0
    resultado = jogar_dados()
    print(f"Primeira jogada: {resultado}")

    if resultado in (7, 11):
        print("Você venceu!")
        return
    elif resultado in (2, 3, 12):
        print("Você perdeu!")
        return

    ponto = resultado
    print(f"Seu ponto é: {ponto}")

    while 1:
        nova_jogada = jogar_dados()
        print(f"Você tirou: {nova_jogada}")
        
        if nova_jogada == ponto:
            print("Você venceu!")
            return
        elif nova_jogada == 7:
            print("Você perdeu!")
            return

jogar_craps()