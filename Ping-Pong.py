from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_y, player_speed, w, h):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.y = player_y

    def reset(self):           
        mw.blit(self.image, (self.rect.y))

class Player(GameSprite):            
    def update(self):                
        keys = key.get_pressed()     
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_width = 1000
win_height = 600
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong")
window.fill((200,255,255))
#fon = transform.scale(image.load('tree.jpg'), (win_width, win_height))

clock = time.Clock()
FPS = 60
game = True
#rocket1 = Player()

ball = GameSprite('ball.png', win_width/2, win_height/2, (4,4), 40,40)
rock1 = Player('stick.png',10,win_height/2, 7, 10, 50)
rock2 = Player('stick2.png',10,win_height/2, 7, 10, 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = quit()

    window.fill((200,255,255))

    ball.rect.x += ball.speed[0]
    ball.rect.y += ball.speed[1]

    if ball.rect.y < 0 or ball.rect.y > win_height-40:
        ball.speed[1] *= -1

    if sprite.collide_rect(ball, rock2) or \
        sprite.collide_rect(ball, rock1):
            ball.speed[1] *= -1
            ball.speed[0] *= -1 

    ball.reset()

    rock2.update_r()
    rock1.update_l()
    rock1.reset()
    rock2.reset()

    display.update()
    clock.tick(FPS)













