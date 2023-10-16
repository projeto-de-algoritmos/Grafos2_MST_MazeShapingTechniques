import pygame, sys
from celula import *
from botao import Botao
from collections import defaultdict

pygame.font.init()
pygame.display.init()
pygame.mixer.init()


WIDTH, HEIGHT = 1280, 720
TILE = 40
# WIDTH, HEIGHT = 900, 900
# TILE = 300
colunas, linhas = WIDTH // TILE, HEIGHT // TILE

clock = pygame.time.Clock()

tela = pygame.display.set_mode((WIDTH + 300, HEIGHT))
pygame.display.set_caption("MazeShapingTechniques - Menu Principal")

fundo_menu = pygame.image.load("../assets/fundo_menu.png")

# Define a trilha sonora
trilha_sonora = True
efeitos_sonoros = True
som_clique = pygame.mixer.Sound("../assets/button_click.wav")


def get_fonte(tamanho):
    return pygame.font.Font("../assets/font.ttf", tamanho)


def tocar_som(efeitos_sonoros, efeito):
    if efeitos_sonoros:
        efeito.play()


def som_derrota(efeitos_sonoros):
    if efeitos_sonoros:
        efeito = pygame.mixer.Sound("../assets/lose.mp3")
        pygame.mixer.Channel(0).play(efeito)


def som_vitoria(efeitos_sonoros):
    if efeitos_sonoros:
        efeito = pygame.mixer.Sound("../assets/win.mp3")
        pygame.mixer.Channel(0).play(efeito)


def menu_principal():
    global trilha_sonora, efeitos_sonoros

    texto_menu = get_fonte(70).render("MazeShapingTechniques", True, "#ffffff")
    rect_menu = texto_menu.get_rect(center=(790, 100))

    botao_play = Botao(fundo=None, posicao=(790, 400), texto_base="JOGAR", fonte=get_fonte(75), cor_base="#e3e3e3", cor_selecao="#ffffff")
    botao_sair = Botao(fundo=None, posicao=(790, 550), texto_base="SAIR", fonte=get_fonte(75), cor_base="#e3e3e3", cor_selecao="#ffffff")

    while True:
        botao_trilha_sonora = Botao(fundo=None, posicao=(1300, 630), texto_base="sons: on" if trilha_sonora else "sons: off", fonte=get_fonte(30), cor_base="#e3e3e3", cor_selecao="#ffffff")
        botao_efeitos_sonoros = Botao(fundo=None, posicao=(1350, 660), texto_base="efeitos: on" if efeitos_sonoros else "efeitos: off", fonte=get_fonte(30), cor_base="#e3e3e3", cor_selecao="#ffffff")

        tela.blit(fundo_menu, (0, 0))
        tela.blit(texto_menu, rect_menu)

        posicao_mouse = pygame.mouse.get_pos()

        for botao in [botao_play, botao_sair, botao_trilha_sonora, botao_efeitos_sonoros]:
            botao.mudarCor(posicao_mouse)
            botao.atualizar(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_play.checarEntrada(posicao_mouse):
                    tocar_som(efeitos_sonoros, som_clique)
                    return
                if botao_sair.checarEntrada(posicao_mouse):
                    pygame.quit()
                    sys.exit()
                if botao_trilha_sonora.checarEntrada(posicao_mouse):
                    tocar_som(efeitos_sonoros, som_clique)
                    trilha_sonora = not trilha_sonora
                    if trilha_sonora: pygame.mixer.music.unpause()
                    else: pygame.mixer.music.pause()
                if botao_efeitos_sonoros.checarEntrada(posicao_mouse):
                    tocar_som(efeitos_sonoros, som_clique)
                    efeitos_sonoros = not efeitos_sonoros

        pygame.display.update()


def menu_algoritmo():
    global efeitos_sonoros

    texto_menu = get_fonte(40).render("Selecione o algoritmo", True, "#ffffff")
    rect_menu = texto_menu.get_rect(center=(790, 75))

    botao_kruskal = Botao(fundo=None, posicao=(790, 300), texto_base="KRUSKAL", fonte=get_fonte(75), cor_base="#e3e3e3", cor_selecao="#ffffff")
    botao_prim = Botao(fundo=None, posicao=(790, 450), texto_base="PRIM", fonte=get_fonte(75), cor_base="#e3e3e3", cor_selecao="#ffffff")
    botao_dfs = Botao(fundo=None, posicao=(790, 600), texto_base="DFS", fonte=get_fonte(75), cor_base="#e3e3e3", cor_selecao="#ffffff")

    while True:
        tela.blit(fundo_menu, (0, 0))
        tela.blit(texto_menu, rect_menu)

        posicao_mouse = pygame.mouse.get_pos()

        for botao in [botao_kruskal, botao_prim, botao_dfs]:
            botao.mudarCor(posicao_mouse)
            botao.atualizar(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_kruskal.checarEntrada(posicao_mouse):
                    tocar_som(efeitos_sonoros, som_clique)
                    return 0
                if botao_prim.checarEntrada(posicao_mouse):
                    tocar_som(efeitos_sonoros, som_clique)
                    return 1
                if botao_dfs.checarEntrada(posicao_mouse):
                    tocar_som(efeitos_sonoros, som_clique)
                    return 2

        pygame.display.update()


def menu_dificuldade():
    global efeitos_sonoros

    texto_menu = get_fonte(75).render("Dificuldade", True, "#ffffff")
    rect_menu = texto_menu.get_rect(center=(790, 75))

    facil = Botao(fundo=None, posicao=(790, 300), texto_base="Fácil", fonte=get_fonte(40), cor_base="#e3e3e3", cor_selecao="#ffffff")
    medio = Botao(fundo=None, posicao=(790, 450), texto_base="Médio", fonte=get_fonte(40), cor_base="#e3e3e3", cor_selecao="#ffffff")
    dificil = Botao(fundo=None, posicao=(790, 600), texto_base="Difícil", fonte=get_fonte(40), cor_base="#e3e3e3", cor_selecao="#ffffff")

    while True:
        tela.blit(fundo_menu, (0, 0))
        tela.blit(texto_menu, rect_menu)

        posicao_mouse = pygame.mouse.get_pos()

        for botao in [facil, medio, dificil]:
            botao.mudarCor(posicao_mouse)
            botao.atualizar(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if facil.checarEntrada(posicao_mouse):
                    tocar_som(efeitos_sonoros, som_clique)
                    return 99
                if medio.checarEntrada(posicao_mouse):
                    tocar_som(efeitos_sonoros, som_clique)
                    return 50
                if dificil.checarEntrada(posicao_mouse):
                    tocar_som(efeitos_sonoros, som_clique)
                    return 30

        pygame.display.update()


def dfs(matriz_celulas, tela_labirinto):
    celula_atual = matriz_celulas[0]
    objetivo = matriz_celulas[-1]
    pilha = []

    contador_parada = 1

    global FPS, texto_tempo, rect_tempo, texto_relogio, rect_texto_relogio, texto_recorde, rect_recorde, texto_valor_recorde, rect_valor_recorde

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


def kruskal(matriz_celulas, tela_labirinto):
    # Define a estrutura union-find como um dicionário e seus respectivos metodos
    union_find = defaultdict(list)

    def find(union_find, elemento):
        if union_find[elemento][0] != elemento:
            union_find[elemento][0] = find(union_find, union_find[elemento][0])
        return union_find[elemento][0]

    def union(union_find, a, b):
        if union_find[a][1] < union_find[b][1]:
            union_find[a][0] = b
        elif union_find[b][1] < union_find[a][1]:
            union_find[b][0] = a
        else:
            union_find[b][0] = a
            union_find[a][1] += 1

    objetivo = matriz_celulas[-1]

    # Cria uma lista com todas as arestas da matriz
    arestas = []
    for celula in matriz_celulas:
        vizinhos = celula.checar_vizinhos(matriz_celulas, linhas, colunas, aleatorio=False)
        celula.visitada = True
        for vizinho in vizinhos:
            arestas.append([celula, vizinho])

    # Cria uma arvore de profundidade 0 no union find para cada celula
    for celula in matriz_celulas:
        union_find[celula] = [celula, 1]
        celula.visitada = False


    global FPS, texto_tempo, rect_tempo, texto_relogio, rect_texto_relogio, texto_recorde, rect_recorde, texto_valor_recorde, rect_valor_recorde

    # Enquanto ainda tem arestas na lista
    while arestas:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Escolhe uma aresta aleatória e remove ela da lista
        celula_atual, proxima_celula = choice(arestas)
        celula_atual.visitada = True
        proxima_celula.visitada = True
        arestas.remove([celula_atual, proxima_celula])

        # Desenha as celulas
        [celula.desenhar(tela, cor="white", TILE=TILE) for celula in matriz_celulas]

        # Desenha a celula atual e a de objetivo
        celula_atual.preencher_celula(tela=tela, cor='red', TILE=TILE)
        objetivo.preencher_celula(tela=tela, cor='green', TILE=TILE)

        # Faz o find das células da aresta atual
        find_atual = find(union_find, celula_atual)
        find_prox = find(union_find, proxima_celula)

        # Se elas forem de arvores diferentes, remove a parede entre elas e faz o union
        if find_atual != find_prox:
            remove_paredes(celula_atual, proxima_celula)
            union(union_find, find_atual, find_prox)

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


def criar_labirinto(algoritmo, qtd_tempo):
    pygame.display.set_caption("MazeShapingTechniques - Modelando Labirinto")

    global FPS
    FPS = 300

    # Preenche a tela inteira e tela do labirinto
    tela_labirinto = pygame.Surface((WIDTH, HEIGHT))
    tela.blit(fundo_menu, (0, 0))
    tela.blit(tela_labirinto, (0, 0))

    # Gera a matriz de celulas
    matriz_celulas = [Celula(coluna, linha) for linha in range(linhas) for coluna in range(colunas)]

    with open('recorde') as f:
        global recorde
        recorde = f.readline()

    # Define o texto do tempo
    global texto_tempo, rect_tempo, texto_relogio, rect_texto_relogio
    texto_tempo = get_fonte(40).render('TEMPO', True, pygame.Color('white'))
    rect_tempo = texto_tempo.get_rect(center=(WIDTH + 150, 50))
    texto_relogio = get_fonte(40).render(f'{qtd_tempo}', True, pygame.Color('white'))
    rect_texto_relogio = texto_relogio.get_rect(center=(WIDTH + 150, 100))

    # Define o texto do recorde
    global texto_recorde, rect_recorde, texto_valor_recorde, rect_valor_recorde
    texto_recorde = get_fonte(40).render('RECORDE', True, pygame.Color('white'))
    rect_recorde = texto_recorde.get_rect(center=(WIDTH + 150, 200))
    texto_valor_recorde = get_fonte(40).render(f'{recorde}', True, pygame.Color('white'))
    rect_valor_recorde = texto_valor_recorde.get_rect(center=(WIDTH + 150, 250))

    # Chama a função específica pro algoritmo selecionado
    match (algoritmo):
        case (0):
            return kruskal(matriz_celulas, tela_labirinto)
        case (1):
            return dfs(matriz_celulas, tela_labirinto)
        case (2):
            return dfs(matriz_celulas, tela_labirinto)


def checa_colisao(rect_jogador, x, y, rect_paredes):
    rect_destino = rect_jogador.move(x, y)
    if rect_destino.collidelist(rect_paredes) == -1:
        return False
    return True


def tela_pausado():
    global pausado, efeitos_sonoros, trilha_sonora

    texto_menu = get_fonte(75).render("PAUSADO", True, "#ffffff")
    rect_menu = texto_menu.get_rect(center=(790, 75))

    botao_continuar = Botao(fundo=None, posicao=(790, 300), texto_base="Continuar", fonte=get_fonte(75), cor_base="#e3e3e3", cor_selecao="#ffffff")
    botao_reiniciar = Botao(fundo=None, posicao=(790, 450), texto_base="Reiniciar", fonte=get_fonte(75), cor_base="#e3e3e3", cor_selecao="#ffffff")

    while True:
        botao_trilha_sonora = Botao(fundo=None, posicao=(1300, 630), texto_base="sons: on" if trilha_sonora else "sons: off", fonte=get_fonte(30), cor_base="#e3e3e3", cor_selecao="#ffffff")
        botao_efeitos_sonoros = Botao(fundo=None, posicao=(1350, 660), texto_base="efeitos: on" if efeitos_sonoros else "efeitos: off", fonte=get_fonte(30), cor_base="#e3e3e3", cor_selecao="#ffffff")

        tela.blit(fundo_menu, (0, 0))
        tela.blit(texto_menu, rect_menu)

        posicao_mouse = pygame.mouse.get_pos()

        for botao in [botao_continuar, botao_reiniciar, botao_trilha_sonora, botao_efeitos_sonoros]:
            botao.mudarCor(posicao_mouse)
            botao.atualizar(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_continuar.checarEntrada(posicao_mouse):
                    tocar_som(efeitos_sonoros, som_clique)
                    pausado = not pausado
                    if trilha_sonora: pygame.mixer.music.unpause()
                    return None
                if botao_reiniciar.checarEntrada(posicao_mouse):
                    return -1
                if botao_trilha_sonora.checarEntrada(posicao_mouse):
                    tocar_som(efeitos_sonoros, som_clique)
                    trilha_sonora = not trilha_sonora
                if botao_efeitos_sonoros.checarEntrada(posicao_mouse):
                    tocar_som(efeitos_sonoros, som_clique)
                    efeitos_sonoros = not efeitos_sonoros

        pygame.display.update()


def jogar(matriz_celulas, tela_labirinto, qtd_tempo):
    pygame.display.set_caption("MazeShapingTechniques - Jogo")

    global FPS, pausado
    # Define o estado do jogo (pausado: bool)
    pausado = False
    FPS = 60

    celula_inicial = matriz_celulas[0]
    objetivo = matriz_celulas[-1]
    rect_objetivo = pygame.Rect(objetivo.x * TILE + 0.50 * TILE, objetivo.y * TILE + 0.50 * TILE, TILE * 0.50, TILE * 0.50)

    # Inicia o relogio de acordo com a dificuldade escolhida e lanca um evento a cada segundo para atualizar ele
    relogio = qtd_tempo
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    global recorde

    # Define o texto do tempo
    global texto_tempo
    rect_tempo = texto_tempo.get_rect(center=(WIDTH + 150, 50))

    # Define o texto do recorde
    global texto_recorde, rect_recorde, texto_valor_recorde, rect_valor_recorde

    # Jogador
    velocidade_jogador = 5
    imagem_jogador = pygame.image.load('../assets/peao.png').convert_alpha()
    imagem_jogador = pygame.transform.scale(imagem_jogador, (TILE - 2 * celula_inicial.espessura, TILE - 2 * celula_inicial.espessura))
    rect_jogador = imagem_jogador.get_rect(center=(TILE // 2, TILE // 2))
    direcoes = {pygame.K_a: (-velocidade_jogador, 0),  pygame.K_d: (velocidade_jogador, 0), pygame.K_w: (0, -velocidade_jogador), pygame.K_s: (0, velocidade_jogador)}
    direcao_atual = (0, 0)

    # Pega os retangulos de todas as paredes do labirinto para tratar colisoes
    rect_paredes = sum([celula.get_rects(TILE) for celula in matriz_celulas], [])

    fonte = get_fonte(40)

    # Cria botão de pause
    global efeitos_sonoros
    botao_pause = Botao(fundo=None, posicao=(1430, 350), texto_base="Pause", fonte=get_fonte(30), cor_base="#e3e3e3", cor_selecao="#ffffff")


    # Definição do som de movimentação
    som_jogador = pygame.mixer.Sound("../assets/jogador_mov.mp3")

    while True:
        if pausado:
            codigo_retorno = tela_pausado()
            if codigo_retorno == -1:
                return -1, -1, -1
        else:
            tela.blit(fundo_menu, (0, 0))
            tela.blit(tela_labirinto, (0, 0))

            posicao_mouse = pygame.mouse.get_pos()
            botao_pause.mudarCor(posicao_mouse)
            botao_pause.atualizar(tela)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.USEREVENT:
                    relogio -= 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_pause.checarEntrada(posicao_mouse):
                        tocar_som(efeitos_sonoros, som_clique)
                        pausado = not pausado
                        pygame.mixer.music.pause()

            # Desenha as celulas
            [celula.desenhar(tela_labirinto, cor="white", TILE=TILE) for celula in matriz_celulas]

            # Desenha as celulas inicial e a de objetivo
            celula_inicial.preencher_celula(tela=tela, cor='red', TILE=TILE)
            objetivo.preencher_celula(tela=tela, cor='green', TILE=TILE)

            # Movimentacao do jogador
            teclas_pressionadas = pygame.key.get_pressed()
            for tecla, direcao in direcoes.items():
                if teclas_pressionadas[tecla] and not checa_colisao(rect_jogador, *direcao, rect_paredes):
                    if direcao != direcao_atual:
                        tocar_som(efeitos_sonoros, som_jogador)
                    direcao_atual = direcao
                    break
            if not checa_colisao(rect_jogador, *direcao_atual, rect_paredes):
                rect_jogador.move_ip(direcao_atual)

            # Verifica se o tempo acabou
            if relogio < 0:
                break

            # Desenha o jogador
            tela.blit(imagem_jogador, rect_jogador)

            # Verifica se o jogador chegou ao objetivo
            if rect_jogador.colliderect(rect_objetivo):
                break

            # Desenha o tempo e o recorde
            texto_relogio = fonte.render(f'{relogio}', True, pygame.Color('white'))
            tela.blit(texto_tempo, rect_tempo)
            tela.blit(texto_relogio, texto_relogio.get_rect(center=(WIDTH + 150, 100)))

            tela.blit(texto_recorde, rect_recorde)
            tela.blit(texto_valor_recorde, rect_valor_recorde)

            pygame.display.update()
            clock.tick(FPS)

    return relogio, recorde, qtd_tempo


def fimdejogo(relogio, recorde, qtd_tempo):
    global efeitos_sonoros

    # Define o novo recorde
    if relogio >= 0:
        recorde = min(int(recorde), qtd_tempo - relogio)
        with open('recorde', 'w') as f:
            f.write(str(recorde))

    # Define os textos do tempo e do recorde
    texto_tempo = get_fonte(55).render(f"Seu tempo: {qtd_tempo - relogio if relogio >= 0 else 0}", True, "#ffffff")
    rect_tempo = texto_tempo.get_rect(center=(790, 250))
    texto_record = get_fonte(55).render(f"Recorde: {recorde}", True, "#ffffff")
    rect_record = texto_record.get_rect(center=(790, 330))

    pygame.display.set_caption("MazeShapingTechniques - Fim de Jogo")

    # Verifica se o jogador ganhou ou perdeu
    pygame.mixer.music.pause()
    if relogio < 0:
        som_derrota(efeitos_sonoros)
        texto = get_fonte(60).render("Você perdeu, que pena :(", True, "#ffffff")
        rect = texto.get_rect(center=(790, 75))
    else:   
        som_vitoria(efeitos_sonoros)
        texto = get_fonte(60).render("Parabéns, você ganhou!", True, "#ffffff")
        rect = texto.get_rect(center=(790, 75))

    botao_play = Botao(fundo=None, posicao=(790, 550), texto_base="JOGAR DE NOVO", fonte=get_fonte(55), cor_base="#e3e3e3", cor_selecao="#ffffff")
    botao_sair = Botao(fundo=None, posicao=(790, 650), texto_base="SAIR", fonte=get_fonte(55), cor_base="#e3e3e3", cor_selecao="#ffffff")


    while True:
        if not pygame.mixer.Channel(0).get_busy(): pygame.mixer.music.unpause()

        tela.blit(fundo_menu, (0, 0))

        posicao_mouse = pygame.mouse.get_pos()

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
                    tocar_som(efeitos_sonoros, som_clique)
                    return
                if botao_sair.checarEntrada(posicao_mouse):
                    pygame.quit()
                    sys.exit()

        

        pygame.display.update()


if __name__ == "__main__":
    while True:
        pygame.mixer.music.load("../assets/soundtrack.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        menu_principal()
        algoritmo = menu_algoritmo()
        qtd_tempo = menu_dificuldade()
        matriz_celulas, tela_labirinto = criar_labirinto(algoritmo, qtd_tempo)
        relogio, recorde, qtd_tempo = jogar(matriz_celulas, tela_labirinto, qtd_tempo)

        # Checa se o jogo foi reiniciado pelo menu de pause
        if relogio == -1 and recorde == -1 and qtd_tempo == -1: continue
