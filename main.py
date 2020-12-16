#!python
import pygame, sys, math, random
from pygame.locals import *

import ship, alien as a, missile, field
import bomb as b


print("Main running")

def screenSetup():
    global SCREEN, fpsClock, initialFPS
    pygame.init()
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 700   
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Pygame Spacies")
    fpsClock = pygame.time.Clock()
    initialFPS = 30

screenSetup()

alienImageA = pygame.image.load("ina.png")
alienImageB = pygame.image.load("inb.png")
fps = initialFPS
TURN_FLEET_LEFT = USEREVENT + 1
TURN_FLEET_RIGHT = USEREVENT + 2
turnLeftEvent = pygame.event.Event(TURN_FLEET_LEFT)
turnRightEvent = pygame.event.Event(TURN_FLEET_RIGHT)
state = "gameState"
TextObject = pygame.font.Font('freesansbold.ttf',32)

myShip = ship.Ship(pygame.image.load("ship.png"), SCREEN.get_width()/2, SCREEN.get_height()-100)
aliens = a.AlienFlotilla([alienImageA,alienImageB],[turnLeftEvent, turnRightEvent]) # array of arrays of Alien objects. All have same direction

listOfBombs=[]
starfield = field.StarField()
while  True:

    if state == "gameState":
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    myShip.direction='left'
                elif event.key == K_RIGHT:
                    myShip.direction = 'right'
                elif event.key == K_SPACE:
                    myShip.fire()
            elif event.type == KEYUP:
                if (event.key == K_LEFT and myShip.direction=='left'):
                    myShip.direction = 'still'
                elif (event.key == K_RIGHT and myShip.direction =='right'):
                    myShip.direction = 'still'
            elif event.type == TURN_FLEET_LEFT:
                aliens.allLeft()
            elif event.type == TURN_FLEET_RIGHT:
                aliens.allRight()

        myShip.update()
        SCREEN.fill((30,50,50))
        starfield.drawStars(SCREEN)
        SCREEN.blit(myShip.sprite,(myShip.x,myShip.y))
        for alien in aliens.fleet:
            alien.update()
            if(random.randint(1,len(aliens.fleet)*50)<=1):
                listOfBombs.append(b.Bomb(alien.x+alien.width/2, alien.y+alien.height))
            SCREEN.blit(alien.sprite,(alien.x, alien.y))

        if len(myShip.missiles)>0:
            for missile in myShip.missiles:
                missile.update()
                for alien in aliens.fleet:
                    if(missile.checkForCollision(alien)== True ):
                        aliens.removeAlien(alien)
                        #Sometimes causes bug... why?colliding with multiple aliens? When hit's the side??
                        try:
                            myShip.missiles.remove(missile)
                        except:
                            print("Two for one???")
                if missile.y <0:
                    try:
                        myShip.missiles.remove(missile)
                    except:
                        print("Error deleting missile")
                SCREEN.blit(missile.sprite,(missile.x,missile.y))
        if len(listOfBombs)>0:
            for bomb in listOfBombs:
                bomb.update()
                
                if(bomb.checkForCollision(myShip)):
                    state = "gameOverState"
                
                SCREEN.blit(bomb.sprite,(bomb.x,bomb.y))
        starfield.update()
        fps = initialFPS + (55-len(aliens.fleet))
        
        pygame.display.update()
        fpsClock.tick(fps)

    elif state == "gameOverState":
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN: 
                if event.key == K_y:
                    print("Trying to play again")
                    myShip = ship.Ship(pygame.image.load("ship.png"), SCREEN.get_width()/2, SCREEN.get_height()-100)
                    aliens = a.AlienFlotilla([alienImageA,alienImageB],[turnLeftEvent, turnRightEvent]) # array of arrays of Alien objects. All have same direction
                    listOfBombs=[]
                    starfield = field.StarField()
                    state = "gameState"
        
        GameOverText = TextObject.render("GAME OVER", False, (150,250,50) )
        PlayAgainText = TextObject.render("To play again press y", False, (150,250,50))
        textRectangle = GameOverText.get_rect()
        textRectangle.center = (600, 200)
        SCREEN.fill((30,50,50))
        SCREEN.blit(GameOverText, textRectangle)
        SCREEN.blit(PlayAgainText, (100,500))
        pygame.display.update()
        fpsClock.tick(fps)
