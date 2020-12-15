import pygame

class StarField:
    
    def __init__(self):
        self.locations = [[50,43],[50, 500],[800,200]]
        self.stable = [[67, 23], [300,42],[560, 346], [76,345]]
        self.description = "My God, it's full of stars"
    
    def update(self):
        for s in self.locations:
            s[1]=(s[1]+1)%800
    # def render(self):
    #     for location in self.locations:
    #         x,y = location
    #         pygame.draw.circle(10,(x,y))
