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
    fire_reload = 30                 
    live = 3                          
                                     
    def update(self):                
        keys = key.get_pressed()     
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 50:
            self.rect.x += self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_SPACE]:       
            if self.fire_reload <= 0:
                self.fire()          
                self.fire_reload = 30

win_width = 600
win_height = 800

mw = display.set_mode((win_width, win_height))
display.set_caption("Star Python Wars")
clock = time.Clock()

fon = transform.scale(image.load('pixilart-drawing.png'), (win_width, win_height))







































































