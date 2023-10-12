import pygame, sys
from celula import *
from botao import Botao

pygame.font.init()
pygame.display.init()

WIDTH, HEIGHT = 1280, 720

tela = pygame.display.set_mode((WIDTH + 300, HEIGHT))
pygame.display.set_caption("MazeShapingTechniques - Menu Principal")
FPS = 100
clock = pygame.time.Clock()

fundo_menu = pygame.image.load("assets/fundo_menu.png")


def get_fonte(tamanho):
    return pygame.font.Font("assets/font.ttf", tamanho)


def menu_principal():
    while True:
        tela.blit(fundo_menu, (0, 0))

        posicao_mouse = pygame.mouse.get_pos()

        texto_menu = get_fonte(70).render("MazeShapingTechniques", True, "#ffffff")
        rect_menu = texto_menu.get_rect(center=(790, 75))

        botao_play = Botao(fundo=None, posicao=(790, 300), texto_base="JOGAR", fonte=get_fonte(75), cor_base="#e3e3e3", cor_selecao="#ffffff")
        botao_opcoes = Botao(fundo=None, posicao=(790, 450), texto_base="OPÇÕES", fonte=get_fonte(75), cor_base="#e3e3e3", cor_selecao="#ffffff")
        botao_sair = Botao(fundo=None, posicao=(790, 600), texto_base="SAIR", fonte=get_fonte(75), cor_base="#e3e3e3", cor_selecao="#ffffff")

        tela.blit(texto_menu, rect_menu)

        for botao in [botao_play, botao_opcoes, botao_sair]:
            botao.mudarCor(posicao_mouse)
            botao.atualizar(tela)

        opcao_escolhida = -1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_play.checarEntrada(posicao_mouse):
                    opcao_escolhida = 0
                    return opcao_escolhida
                if botao_opcoes.checarEntrada(posicao_mouse):
                    opcao_escolhida = 1
                    return opcao_escolhida
                if botao_sair.checarEntrada(posicao_mouse):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def jogar():
    tela = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("MazeShapingTechniques - Jogo")
    TILE = 40
    colunas, linhas = WIDTH // TILE, HEIGHT // TILE

    matriz_celulas = [Celula(coluna, linha) for linha in range(linhas) for coluna in range(colunas)]

    celula_atual = matriz_celulas[0]
    objetivo = matriz_celulas[-1]
    pilha = []

    while True:
        tela.fill(pygame.Color('black'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        [celula.desenhar(tela, cor="white", TILE=TILE) for celula in matriz_celulas]

        celula_atual.visitada = True
        celula_atual.preencher_celula(tela=tela, cor='red', TILE=TILE)
        objetivo.preencher_celula(tela=tela, cor='green', TILE=TILE)

        proxima_celula = celula_atual.checar_vizinhos(matriz_celulas, linhas, colunas)
        if proxima_celula:
            proxima_celula.visitada = True
            pilha.append(celula_atual)
            remove_paredes(celula_atual, proxima_celula)
            celula_atual = proxima_celula
        elif pilha:
            celula_atual = pilha.pop()

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    opcao_escolhida = menu_principal()
    if opcao_escolhida == 0:
        jogar()
    elif opcao_escolhida == 1:
        pygame.quit()
        sys.exit()
