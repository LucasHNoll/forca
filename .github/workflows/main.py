import pygame
import random

# Inicializando o Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Forca")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Fontes
FONTE_GRANDE = pygame.font.SysFont('arial', 36)
FONTE_PEQUENA = pygame.font.SysFont('arial', 24)

# Listas de palavras
animais = ['gato', 'cachorro', 'papagaio', 'elefante', 'tigre', 'leão']
frutas = ['maçã', 'banana', 'cereja', 'laranja', 'uva', 'morango']
objetos = ['caneta', 'livro', 'cadeira', 'mesa', 'televisão', 'geladeira']

conjunto = [animais, frutas, objetos]

def escolher_palavra():
    return random.choice(random.choice(conjunto))

def desenhar_forca(chances):
    if chances < 10:
        pygame.draw.line(tela, PRETO, (100, 500), (100, 100), 10) # Mastro
        pygame.draw.line(tela, PRETO, (50, 500), (150, 500), 10) # Base
        pygame.draw.line(tela, PRETO, (100, 100), (300, 100), 10) # Topo
    if chances < 9:
        pygame.draw.line(tela, PRETO, (300, 100), (300, 150), 10) # Suporte da corda
    if chances < 8:
        pygame.draw.circle(tela, PRETO, (300, 200), 50, 10) # Cabeça
    if chances < 7:
        pygame.draw.circle(tela, PRETO, (285, 190), 5, 10) # Olho Esquerdo
        pygame.draw.circle(tela, PRETO, (315, 190), 5, 10) # Olho Direito
    if chances < 6:
        pygame.draw.arc(tela, PRETO, (275, 210, 50, 20), 3.14, 0, 10) # Boca
    if chances < 5:
        pygame.draw.line(tela, PRETO, (300, 250), (300, 350), 10) # Tronco
    if chances < 4:
        pygame.draw.line(tela, PRETO, (300, 260), (375, 350), 10) # Braço Direito
    if chances < 3:
        pygame.draw.line(tela, PRETO, (300, 260), (225, 350), 10) # Braço Esquerda
    if chances < 2:
        pygame.draw.line(tela, PRETO, (300, 350), (375, 450), 10) # Perna Direita
    if chances < 1:
        pygame.draw.line(tela, PRETO, (300, 350), (225, 450), 10) # Perna Esquerda

def desenhar(palavra, letras_usuario, chances):
    tela.fill(BRANCO)

    palavra_exibida = ""
    for letra in palavra:
        if letra.lower() in letras_usuario:
            palavra_exibida += letra + " "
        else:
            palavra_exibida += "_ "

    palavra_texto = FONTE_GRANDE.render(palavra_exibida.strip(), True, PRETO)
    tela.blit(palavra_texto, (LARGURA // 2 - palavra_texto.get_width() // 8, ALTURA // 3))

    chances_texto = FONTE_PEQUENA.render(f"Chances restantes: {chances}", True, PRETO)
    tela.blit(chances_texto, (20, 20))

    desenhar_forca(chances)

    pygame.display.update()

# Loop principal do jogo
executando = True
while executando:
    palavra = escolher_palavra()
    letras_usuario = []
    chances = 10
    ganhou = False
    jogando = True

    while jogando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executando = False
                jogando = False
            if event.type == pygame.KEYDOWN:
                letra = event.unicode
                if letra.isalpha() and letra not in letras_usuario:
                    letras_usuario.append(letra.lower())
                    if letra.lower() not in palavra.lower():
                        chances -= 1

        desenhar(palavra, letras_usuario, chances)

        ganhou = all(letra.lower() in letras_usuario for letra in palavra)

        if chances == 0 or ganhou:
            jogando = False

    if ganhou:
        mensagem = FONTE_GRANDE.render(f"Parabéns, você ganhou! A palavra era: {palavra}", True, PRETO)
    else:
        mensagem = FONTE_GRANDE.render(f"Você perdeu! A palavra era: {palavra}", True, PRETO)

    tela.fill(BRANCO)
    tela.blit(mensagem, (LARGURA // 2 - mensagem.get_width() // 2, ALTURA // 2))
    pygame.display.update()
    pygame.time.wait(3000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

    opcao = input("Deseja jogar novamente? (sim/não): ")
    if opcao.lower() != "sim":
        executando = False

pygame.quit()
