from pygame import *
font.init()
from random import randint
font.init()
font1 = font.Font(None, 36)

window = display.set_mode((700,500))
display.set_caption("Пинг-понг")

background = transform.scale(
    image.load('phon.png'),
    (700,500))

finish = False
clock = time.Clock()
FPS = 60

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_s] and self.rect.y < -650:
            self.rect.x += self.speed

player =Player('racket.png')



game = True
while game:  
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:


    clock.tick(FPS)       
    display.update()
