import pygame
import missile

class Ship:
    def __init__(self, sprite, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.description = "Space ship"
        self.direction = "still"
        self.sprite = sprite
        self.missiles = []
        self.fireSound = pygame.mixer.Sound("Laser_Shoot4.wav")
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        self.lives = 3

    def update(self):
        if self.direction =='left':
            self.x = max(0, self.x-self.speed)
        elif self.direction == 'right':
            self.x = min(1200-(self.width/2), self.x+self.speed)
    
    def fire(self):
        self.missiles.append(missile.Missile(self.x+(self.width/2), self.y-5 ))
        self.fireSound.play()
