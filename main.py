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
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH,700))
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

IntroState=False
GameState=True
GameOverState = False
myShip = ship.Ship(pygame.image.load("ship.png"))
aliens = a.AlienFlotilla([alienImageA,alienImageB],[turnLeftEvent, turnRightEvent]) # array of arrays of Alien objects. All have same direction

listOfBombs=[]
starfield = field.StarField()
while GameState == True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            #Key down and key up direction changes need to be refactored
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
    for star in starfield.locations:
        x,y = star
        pygame.draw.circle(SCREEN, (200,200,200), (x,y), 3)
    for star in starfield.stable:
        x,y = star
        pygame.draw.circle(SCREEN, (150,150,150),(x,y), 2)
    SCREEN.blit(myShip.sprite,(myShip.x,myShip.y))
    for alien in aliens.fleet:
        alien.update()
        # I dont think this should be here, and I want to cheat and mod the prob of dropping a bomb
        # depending how many aliens there are
        if(random.randint(1,len(aliens.fleet)*50)==1):
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
            #This can be 
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
                GameState = False
                GameOverState = True
            SCREEN.blit(bomb.sprite,(bomb.x,bomb.y))
    starfield.update()
    fps = initialFPS + (55-len(aliens.fleet))
    
    pygame.display.update()
    fpsClock.tick(fps)

while GameOverState == True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN: 
            if event.key == K_y:
                print("Trying to play again")
                myShip = ship.Ship(pygame.image.load("ship.png"))
                aliens = a.AlienFlotilla([alienImageA,alienImageB],[turnLeftEvent, turnRightEvent]) # array of arrays of Alien objects. All have same direction
                listOfBombs=[]
                starfield = field.StarField()
                GameOverState = False
                GameState = True
    TextObject = pygame.font.Font('freesansbold.ttf',32)
    GameOverText = TextObject.render("GAME OVER", True, (150,250,50) )
    textRectangle = GameOverText.get_rect()
    textRectangle.center = (600, 200)
    SCREEN.fill((30,50,50))
    SCREEN.blit(GameOverText, textRectangle)
    pygame.display.update()
    fpsClock.tick(fps)
