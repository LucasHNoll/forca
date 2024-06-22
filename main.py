# forca
import random

animais = ['gato', 'cachorro', 'papagaio', 'elefante', 'tigre', 'leão']
frutas = ['maçã', 'banana', 'cereja', 'laranja', 'uva', 'morango']
objetos = ['caneta', 'livro', 'cadeira', 'mesa', 'televisão', 'geladeira']

conjunto = [animais, frutas, objetos]

while True:
    palavra = random.choice(random.choice(conjunto))
    letras_usuario = []
    chances = 10
    ganhou = False
    opção = "sim"

    while opção == "sim":
        for letra in palavra:
            if letra.lower() in letras_usuario:
                print(letra, end=" ")
            else:
                print("_", end=" ")

        print(f"Você tem {chances} chances")

        tentativa = input("Escolha uma letra para adivinhar: ")

        letras_usuario.append(tentativa.lower())

        if tentativa.lower() not in palavra.lower():
            chances -= 1

        ganhou = all(letra.lower() in letras_usuario for letra in palavra)

        if chances == 0 or ganhou:
            break

    if ganhou:
        print(f"Parabéns, você ganhou. A palavra era: {palavra}")

    else:
        print(f"Você perdeu! A palavra era: {palavra}")

    opção = input("Deseja jogar novamente? (sim/não): ")
    if opção != "sim":
        break

#fecha o repit da próxima vez-_-# forca
