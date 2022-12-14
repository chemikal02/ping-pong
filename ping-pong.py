from pygame import *
from random import randint


font.init()
font1 = font.Font(None, 36)
lose1 = font1.render(
    'PLAYER 1 LOSE!', True, (180, 0 , 0))

font2 = font.Font(None, 36)
lose2 = font1.render(
    'PLAYER 2 LOSE!', True, (180, 0 , 0))

window = display.set_mode((700,500))
display.set_caption("Пинг-понг")

background = transform.scale(
    image.load('phon.jpg'),
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
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.x < 650:
            self.rect.y += self.speed

player = Player('biba.png', 600, 250, 5)

class Player2(GameSprite):
    def __init__(self, player2_image, player2_x, player2_y, player2_speed):
        super().__init__(player2_image, player2_x, player2_y, player2_speed)
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.x < 650:
            self.rect.y += self.speed

player2 = Player2('rocket_1_prev_ui.png', 20, 250, 5)
            
ball = GameSprite('ball_prev_ui.png', 300, 250, 5)

speed_x = 5
speed_y = 5

win_height = 500
win_width = 700

game = True
while game:  
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 5:
            ball.rect.y -= ball.speed
        if ball.rect.y < 450:
            ball.rect.y += ball.speed
        if ball.rect.x > 5:
            ball.rect.x -= ball.speed
        if ball.rect.x < 650:
            ball.rect.x += ball.speed  

        window.blit(background, (0,0)) 
        ball.reset()
        player.reset()
        player.update()
        player2.reset()
        player2.update()
    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
        speed_y *= -1    
    if ball.rect.x > win_width - 50 or ball.rect.x < 0:
        speed_x *= -1  

    if sprite.collide_rect(player, ball):
        window.blit(lose2,(200, 200))
        finish = True
    if sprite.collide_rect(player2, ball):
        window.blit(lose1,(200, 200))
        finish = True

    clock.tick(FPS)       
    display.update()
