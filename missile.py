import pygame
##What if I DON'T import pygame here and instead pass the sprite in from the main program in the constructor??

class Missile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load('green_missile.png')
        self.explosionSound = pygame.mixer.Sound("Explosion2.wav")

    def update(self):
        self.y = self.y - 10

    def checkForCollision(self, alien):
        if(self.x > alien.x and self.x < alien.x+alien.width and self.y <= alien.y+alien.height and self.y >= alien.y):
            self.explosionSound.play()
            return True
        else:
            return False

class Bomb:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load("green_missile.png")
        self.height = self.sprite.get_height()
    
    def update(self):
        self.y +=10

    def checkForCollision(self, player):
        if (self.y+self.height) >=player.y:
            if self.x > player.x and self.x<player.x+player.width and self.y> player.y+player.height:
                return True
        return False
