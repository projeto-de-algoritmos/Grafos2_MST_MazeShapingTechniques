import pygame, sys
from celula import *
from botao import Botao

pygame.font.init()
pygame.display.init()

WIDTH, HEIGHT = 1280, 720
TILE = 40

tela = pygame.display.set_mode((WIDTH + 300, HEIGHT))
pygame.display.set_caption("MazeShapingTechniques - Menu Principal")
clock = pygame.time.Clock()

fundo_menu = pygame.image.load("../assets/fundo_menu.png")


def get_fonte(tamanho):
    return pygame.font.Font("../assets/font.ttf", tamanho)


def menu_principal():
    while True:
        tela.blit(fundo_menu, (0, 0))

        posicao_mouse = pygame.mouse.get_pos()

        texto_menu = get_fonte(70).render("MazeShapingTechniques", True, "#ffffff")
        rect_menu = texto_menu.get_rect(center=(790, 100))

        botao_play = Botao(fundo=None, posicao=(790, 400), texto_base="JOGAR", fonte=get_fonte(75), cor_base="#e3e3e3", cor_selecao="#ffffff")
        botao_sair = Botao(fundo=None, posicao=(790, 550), texto_base="SAIR", fonte=get_fonte(75), cor_base="#e3e3e3", cor_selecao="#ffffff")

        tela.blit(texto_menu, rect_menu)

        for botao in [botao_play, botao_sair]:
            botao.mudarCor(posicao_mouse)
            botao.atualizar(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_play.checarEntrada(posicao_mouse):
                    return
                if botao_sair.checarEntrada(posicao_mouse):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def menu_algoritmo():
    while True:
        tela.blit(fundo_menu, (0, 0))

        posicao_mouse = pygame.mouse.get_pos()

        texto_menu = get_fonte(40).render("Selecione o algoritmo", True, "#ffffff")
        rect_menu = texto_menu.get_rect(center=(790, 75))

        botao_kruskal = Botao(fundo=None, posicao=(790, 300), texto_base="KRUSKAL", fonte=get_fonte(75), cor_base="#e3e3e3", cor_selecao="#ffffff")
        botao_prim = Botao(fundo=None, posicao=(790, 450), texto_base="PRIM", fonte=get_fonte(75), cor_base="#e3e3e3", cor_selecao="#ffffff")
        botao_dfs = Botao(fundo=None, posicao=(790, 600), texto_base="DFS", fonte=get_fonte(75), cor_base="#e3e3e3", cor_selecao="#ffffff")

        tela.blit(texto_menu, rect_menu)

        for botao in [botao_kruskal, botao_prim, botao_dfs]:
            botao.mudarCor(posicao_mouse)
            botao.atualizar(tela)

        algoritmo_escolhido = -1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_kruskal.checarEntrada(posicao_mouse):
                    algoritmo_escolhido = 0
                    return algoritmo_escolhido
                if botao_prim.checarEntrada(posicao_mouse):
                    algoritmo_escolhido = 1
                    return algoritmo_escolhido
                if botao_dfs.checarEntrada(posicao_mouse):
                    algoritmo_escolhido = 2
                    return algoritmo_escolhido
                
        pygame.display.update()


def criar_labirinto(algoritmo):
    pygame.display.set_caption("MazeShapingTechniques - Modelando Labirinto")

    FPS = 300

    # Preenche a tela inteira e tela do labirinto
    tela_labirinto = pygame.Surface((WIDTH, HEIGHT))
    tela.blit(fundo_menu, (0, 0))
    tela.blit(tela_labirinto, (0, 0))

    # Gera a matriz de celulas
    colunas, linhas = WIDTH // TILE, HEIGHT // TILE

    matriz_celulas = [Celula(coluna, linha) for linha in range(linhas) for coluna in range(colunas)]

    # Define as celula atual como a primeira e a celula de objetivo com a ultima, alem de uma pilha pra dfs
    celula_atual = matriz_celulas[0]
    objetivo = matriz_celulas[-1]
    pilha = []

    contador_parada = 1

    with open('recorde') as f:
        global recorde
        recorde = f.readline()

    # Define o texto do tempo
    global texto_tempo
    texto_tempo = get_fonte(40).render('TEMPO', True, pygame.Color('white'))
    rect_tempo = texto_tempo.get_rect(center=(WIDTH + 150, 50))
    texto_relogio = get_fonte(40).render('60', True, pygame.Color('white'))
    rect_texto_relogio = texto_relogio.get_rect(center=(WIDTH + 150, 100))

    # Define o texto do recorde
    global texto_recorde, rect_recorde, texto_valor_recorde, rect_valor_recorde
    texto_recorde = get_fonte(40).render('RECORDE', True, pygame.Color('white'))
    rect_recorde = texto_recorde.get_rect(center=(WIDTH + 150, 200))
    texto_valor_recorde = get_fonte(40).render(f'{recorde}', True, pygame.Color('white'))
    rect_valor_recorde = texto_valor_recorde.get_rect(center=(WIDTH + 150, 250))

    # Roda ate finalizar a matriz
    while contador_parada != len(matriz_celulas):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Desenha as celulas
        [celula.desenhar(tela, cor="white", TILE=TILE) for celula in matriz_celulas]

        # Define a celula atual como visitada e desenha ela e a de objetivo
        celula_atual.visitada = True
        celula_atual.preencher_celula(tela=tela, cor='red', TILE=TILE)
        objetivo.preencher_celula(tela=tela, cor='green', TILE=TILE)

        # Escolhe uma vizinha aleatoria para seguir e remove a parede entre elas
        proxima_celula = celula_atual.checar_vizinhos(matriz_celulas, linhas, colunas)
        if proxima_celula:
            proxima_celula.visitada = True
            pilha.append(celula_atual)
            remove_paredes(celula_atual, proxima_celula)
            celula_atual = proxima_celula
            contador_parada += 1
        elif pilha:
            celula_atual = pilha.pop()

        # Desenha o tempo e o recorde
        tela.blit(texto_tempo, rect_tempo)
        tela.blit(texto_relogio, rect_texto_relogio)

        tela.blit(texto_recorde, rect_recorde)
        tela.blit(texto_valor_recorde, rect_valor_recorde)

        pygame.display.update()
        clock.tick(FPS)

    # Roda mais um frame para transição pra gameplay ficar mais fluída    
    [celula.desenhar(tela, cor="white", TILE=TILE) for celula in matriz_celulas]
    matriz_celulas[0].preencher_celula(tela=tela, cor='red', TILE=TILE)
    pygame.display.update()
    clock.tick(FPS)

    return matriz_celulas, tela_labirinto


def fimdejogo(relogio, recorde):
    # Define o novo recorde
    if relogio >= 0:
        recorde = min(int(recorde), 60 - relogio)
        with open('recorde', 'w') as f:
            f.write(str(recorde))

    # Define os textos do tempo e do recorde
    texto_tempo = get_fonte(55).render(f"Seu tempo: {60 - relogio if relogio >= 0 else 0}", True, "#ffffff")
    rect_tempo = texto_tempo.get_rect(center=(790, 250))
    texto_record = get_fonte(55).render(f"Recorde: {recorde}", True, "#ffffff")
    rect_record = texto_record.get_rect(center=(790, 300))

    pygame.display.set_caption("MazeShapingTechniques - Fim de Jogo")

    # Verifica se o jogador ganhou ou perdeu
    if relogio < 0:
        texto = get_fonte(60).render("Você perdeu, que pena :(", True, "#ffffff")
        rect = texto.get_rect(center=(790, 75))
    else:
        texto = get_fonte(60).render("Parabéns, você ganhou!", True, "#ffffff")
        rect = texto.get_rect(center=(790, 75))

    while True:
        tela.blit(fundo_menu, (0, 0))

        posicao_mouse = pygame.mouse.get_pos()

        botao_play = Botao(fundo=None, posicao=(790, 550), texto_base="JOGAR DE NOVO", fonte=get_fonte(55), cor_base="#e3e3e3", cor_selecao="#ffffff")
        botao_sair = Botao(fundo=None, posicao=(790, 650), texto_base="SAIR", fonte=get_fonte(55), cor_base="#e3e3e3", cor_selecao="#ffffff")

        tela.blit(texto, rect)
        tela.blit(texto_tempo, rect_tempo)
        tela.blit(texto_record, rect_record)

        for botao in [botao_play, botao_sair]:
            botao.mudarCor(posicao_mouse)
            botao.atualizar(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_play.checarEntrada(posicao_mouse):
                    return
                if botao_sair.checarEntrada(posicao_mouse):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def jogar(matriz_celulas, tela_labirinto):
    pygame.display.set_caption("MazeShapingTechniques - Jogo")

    FPS = 60

    celula_inicial = matriz_celulas[0]
    objetivo = matriz_celulas[-1]

    # Inicia o relogio em 60 e lanca um evento a cada segundo para atualizar ele
    relogio = 60
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    global recorde

    # Define o texto do tempo
    global texto_tempo
    rect_tempo = texto_tempo.get_rect(center=(WIDTH + 150, 50))

    # Define o texto do recorde
    global texto_recorde, rect_recorde, texto_valor_recorde, rect_valor_recorde

    while True:
        tela.blit(fundo_menu, (0, 0))
        tela.blit(tela_labirinto, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.USEREVENT:
                relogio -= 1

        # Desenha as celulas
        [celula.desenhar(tela, cor="white", TILE=TILE) for celula in matriz_celulas]

        # Desenha as celulas inicial e a de objetivo
        celula_inicial.preencher_celula(tela=tela, cor='red', TILE=TILE)
        objetivo.preencher_celula(tela=tela, cor='green', TILE=TILE)

        # Verifica se o tempo acabou
        if relogio < 0:
            break

        # Desenha o tempo e o recorde
        texto_relogio = get_fonte(40).render(f'{relogio}', True, pygame.Color('white'))
        tela.blit(texto_tempo, rect_tempo)
        tela.blit(texto_relogio, texto_relogio.get_rect(center=(WIDTH + 150, 100)))

        tela.blit(texto_recorde, rect_recorde)
        tela.blit(texto_valor_recorde, rect_valor_recorde)

        pygame.display.update()
        clock.tick(FPS)

    return relogio, recorde


if __name__ == "__main__":
    while True:
        menu_principal()
        algoritmo = menu_algoritmo()
        matriz_celulas, tela_labirinto = criar_labirinto(algoritmo)
        relogio, recorde = jogar(matriz_celulas, tela_labirinto)
        fimdejogo(relogio, recorde)
