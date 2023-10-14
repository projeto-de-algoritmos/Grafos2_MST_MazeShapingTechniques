class Botao():
    def __init__(self, fundo, posicao, texto_base, fonte, cor_base, cor_selecao):
        self.fundo = fundo
        self.x = posicao[0]
        self.y = posicao[1]
        self.texto_base = texto_base
        self.fonte = fonte
        self.cor_base = cor_base
        self.cor_selecao = cor_selecao
        self.texto = self.fonte.render(self.texto_base, True, self.cor_base)
        if self.fundo is None:
            self.fundo = self.texto
        self.rect = self.fundo.get_rect(center=(self.x, self.y))
        self.rect_texto = self.texto.get_rect(center=(self.x, self.y))

    def atualizar(self, tela):
        if self.fundo is not None:
            tela.blit(self.fundo, self.rect)
        tela.blit(self.texto, self.rect_texto)

    def checarEntrada(self, posicao):
        if posicao[0] in range(self.rect.left, self.rect.right) and posicao[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def mudarCor(self, posicao):
        if posicao[0] in range(self.rect.left, self.rect.right) and posicao[1] in range(self.rect.top, self.rect.bottom):
            self.texto = self.fonte.render(self.texto_base, True, self.cor_selecao)
        else:
            self.texto = self.fonte.render(self.texto_base, True, self.cor_base)
