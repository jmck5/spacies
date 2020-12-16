import pygame
import random

class Alien:
    def __init__ (self, sprites, x, y, events):
        self.x = x
        self.y = y
        self.sprites = sprites
        self.sprite = self.sprites[0]
        self.direction = 'right'
        self.speed = 5
        self.counter=0
        self.turnLeftSignal = events[0]
        self.turnRightSignal = events[1]
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.attackThreshold = 10
        self.attackProbDenominator = 1000

    def update(self):
        

        if self.direction == 'right':
            self.x = self.x + self.speed
        elif self.direction == 'left':
            self.x = self.x - self.speed
        
        if self.direction =='right' and self.x > 1200-self.width:
            
            pygame.event.post(self.turnLeftSignal)
            
        elif self.direction =='left' and self.x < 0:
            
            pygame.event.post(self.turnRightSignal)

        if ((self.sprite == self.sprites[0]) and (self.counter >= 15)):
                self.sprite = self.sprites[1]
                self.counter=0
        elif ((self.sprite == self.sprites[1]) and (self.counter >= 15)):
                self.sprite = self.sprites[0]
                self.counter=0

        self.counter += 1
        
class AlienFlotilla:
    def __init__(self, sprites, events):
        self.fleet = []
        alienImageA = sprites[0]
        alienImageB = sprites[1]

        for y in range(5):
            for x in range(11):
                #When destroyed can pop from a python index 
                self.addAlien(Alien(sprites, x*70+10, y*50+10, events))
        self.direction ='RIGHT'

    def addAlien(self, alien):
        self.fleet.append(alien)
    
    def removeAlien(self, alien):
        self.fleet.remove(alien)

    def switchDirection(self):
        if self.direction=='RIGHT':
            self.direction = 'LEFT'
            for ship in self.fleet:
                ship.direction = 'left'
                ship.y+=2
        elif self.direction=='LEFT':
            self.direction='RIGHT'
            for ship in self.fleet:
                ship.direction='right'
                ship.y+=2
    
    def allLeft(self):
        for ship in self.fleet:
            ship.direction = 'left'
            ship.y+=5

    def allRight(self):
        for ship in self.fleet:
            ship.direction = 'right'
            ship.y+=5
            
