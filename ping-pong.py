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

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = 4
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

    

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_s] and self.rect.y < -650:
            self.rect.x += self.speed

player = Player('racket.png' 20, 400, 5)

class Player2(GameSprite):
    def __init__(self, player2_image, player2_x, player2_y, player2_speed):
        super().__init__(player2_image, player2_x, player2_y, player2_speed)
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < -650:
            self.rect.x += self.speed

player2 = Player('racket.png1', 20, 20, 5)
            
ball = GameSprite(ball.jpg)



game = True
while game:  
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y -= speed_y


    clock.tick(FPS)       
    display.update()
