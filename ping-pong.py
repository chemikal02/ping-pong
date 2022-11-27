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





game = True
while game:  
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:


    clock.tick(FPS)       
    display.update()
