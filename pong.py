#Создай собственный Шутер!
from pygame import *

#создай окно игры
window = display.set_mode((700,500))
display.set_caption('ААААААААААА')
clock = time.Clock()
FPS = 60
background = transform.scale(image.load('foooooon.png'), (700, 500))

font.init()
font2 = font.SysFont("Arial", 36)
font3 = font.SysFont("Arial", 100)

#классы
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y):
        super().__init__()    
        self.image = transform.scale(image.load(player_image), (20, 100))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def xodim(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= 8
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += 8

    def xodim2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 8
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += 8


player1 = Player('platforma.png', 5, 250)
player2 = Player('platforma.png', 675, 250)
game = True
while game:
    window.blit(background, (0,0))
    player1.reset()
    player2.reset()
    player2.xodim()
    player1.xodim2()

    for e in event.get():
        if e.type == QUIT:
            game= False

    clock.tick(FPS)
    display.update()