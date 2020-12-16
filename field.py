import pygame

class StarField:
    
    def __init__(self):
        self.locations = [[537,260],[1098,236],[39,221],[672,412],[1035,620],[322,685],[369,352],[305,25],[1002,630],[89,96],]
        self.stable = [[706,277],[708,507],[431,486],[1062,469],[407,316],[1163,374],[207,216],[359,237],[641,194],[1036,660],]
        self.description = "My God, it's full of stars"
    
    def update(self):
        for s in self.locations:
            s[1]=(s[1]+1)%800
    # def render(self):
    #     for location in self.locations:
    #         x,y = location
    #         pygame.draw.circle(10,(x,y))
    def drawStars(self,SCREEN):
        for star in self.locations:
            x,y = star
            pygame.draw.circle(SCREEN, (200,200,200), (x,y), 2)
        for star in self.stable:
            x,y = star
            pygame.draw.circle(SCREEN, (150,150,150),(x,y), 2)