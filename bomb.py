import pygame

class Bomb:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load("red_bomb.png")
        self.height = self.sprite.get_height()
    
    def update(self):
        self.y +=10

    def checkForCollision(self, player):
        if (self.y+self.height) >=player.y:
            if self.x > player.x and self.x<player.x+player.width and self.y< player.y+player.height:
                return True
        return False



