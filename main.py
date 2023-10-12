import pygame
from random import choice

# Define a resolucao, tamanho do lado de cada quadrado e numero de linhas e colunas
RES = WIDTH, HEIGHT = 1280, 720
TILE = 40
colunas, linhas = WIDTH // TILE, HEIGHT // TILE


# Classe para cada celula da matriz
class Celula:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.paredes = {"cima": True, "direita": True, "baixo": True, "esquerda": True}
        self.visitada = False
        self.espessura = 4

    def preencher_celula(self, tela, cor):
        x, y = self.x * TILE, self.y * TILE
        pygame.draw.rect(tela, pygame.Color(cor), (x + self.espessura - 0.5, y + self.espessura - 0.5, TILE - self.espessura + 0.5, TILE - self.espessura + 0.5))

    def desenhar(self, tela, cor):
        x, y = self.x * TILE, self.y * TILE
        if self.visitada:
            pygame.draw.rect(tela, pygame.Color(cor), (x, y, TILE, TILE))

        if self.paredes["cima"]:
            pygame.draw.line(tela, pygame.Color("black"), (x, y), (x + TILE, y), self.espessura)

        if self.paredes["direita"]:
            pygame.draw.line(tela, pygame.Color("black"), (x + TILE, y), (x + TILE, y + TILE), self.espessura)

        if self.paredes["baixo"]:
            pygame.draw.line(tela, pygame.Color("black"), (x + TILE, y + TILE), (x, y + TILE), self.espessura)

        if self.paredes["esquerda"]:
            pygame.draw.line(tela, pygame.Color("black"), (x, y + TILE), (x, y), self.espessura)

    def checar_celula(self, x, y, matriz_celulas):
        procura_indice = lambda x, y: x + y * colunas
        if x < 0 or x > colunas - 1 or y < 0 or y > linhas - 1 or matriz_celulas[procura_indice(x, y)].visitada is True:
            return False
        return matriz_celulas[procura_indice(x, y)]

    def checar_vizinhos(self, matriz_celulas):
        vizinhos = []
        cima = self.checar_celula(self.x, self.y - 1, matriz_celulas)
        direita = self.checar_celula(self.x + 1, self.y, matriz_celulas)
        baixo = self.checar_celula(self.x, self.y + 1, matriz_celulas)
        esquerda = self.checar_celula(self.x - 1, self.y, matriz_celulas)
        if cima:
            vizinhos.append(cima)
        if direita:
            vizinhos.append(direita)
        if baixo:
            vizinhos.append(baixo)
        if esquerda:
            vizinhos.append(esquerda)

        return choice(vizinhos) if vizinhos else False


def remove_paredes(atual, proxima):
    dx = atual.x - proxima.x
    dy = atual.y - proxima.y
    if dx == 1:
        atual.paredes['esquerda'] = False
        proxima.paredes['direita'] = False
    elif dx == -1:
        atual.paredes['direita'] = False
        proxima.paredes['esquerda'] = False
    if dy == 1:
        atual.paredes['cima'] = False
        proxima.paredes['baixo'] = False
    elif dy == -1:
        atual.paredes['baixo'] = False
        proxima.paredes['cima'] = False


def jogo():
    FPS = 100
    tela = pygame.display.set_mode(RES)
    pygame.display.set_caption("MazeShapingTechniques")
    clock = pygame.time.Clock()

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

        [celula.desenhar(tela, cor="white") for celula in matriz_celulas]

        celula_atual.visitada = True
        celula_atual.preencher_celula(tela=tela, cor='red')
        objetivo.preencher_celula(tela=tela, cor='green')

        proxima_celula = celula_atual.checar_vizinhos(matriz_celulas)
        if proxima_celula:
            proxima_celula.visitada = True
            pilha.append(celula_atual)
            remove_paredes(celula_atual, proxima_celula)
            celula_atual = proxima_celula
        elif pilha:
            celula_atual = pilha.pop()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    jogo()
