import pygame

pygame.init()
tela_largura = 1000
tela_altura = int(690)

tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption('SURVIVE')

relogio = pygame.time.Clock()
FPS = 60

movimento_cima = False
movimento_baixo = False
movimento_esquerda = False
movimento_direita = False

BG = (233,212,96,1)

def desenho_bg():
    tela.fill(BG)

class Player(pygame.sprite.Sprite):
    def __init__(self, x,y,scale,speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direcao = 1
        self.virar = False
        img = pygame.image.load('Survivey//img////player//francis_champ.gif')
        self.image = pygame.transform.scale(img,(int(img.get_width()* scale),(int(img.get_height()*  scale))))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def moves(self,movimento_esquerda, movimento_direita):
        dx = 0
        dy = 0

        if movimento_esquerda:
            dx = - self.speed
            self.virar = False
            self.direcao = 1
        if movimento_direita:
            dx = self.speed
            self.virar = True
            self.direcao = -1
        self.rect.x +=dx
        self.rect.y +=dy

    def desenho(self):
        tela.blit(pygame.transform.flip(self.image, self.virar, False), self.rect)
        


jogador1 = Player(950,250,1,5)


run=True
while run:
    relogio.tick(FPS)
    desenho_bg()
    jogador1.desenho()
    jogador1.moves(movimento_esquerda,movimento_direita)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    movimento_esquerda=True

                if event.key == pygame.K_d:
                    movimento_direita=True    

                if event.key == pygame.K_ESCAPE:
                    run = False

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    movimento_esquerda=False

                if event.key == pygame.K_d:
                    movimento_direita=False
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
