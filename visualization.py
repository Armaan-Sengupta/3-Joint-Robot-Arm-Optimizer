from main import *
import math
import time

WIDTH=800  
HEIGHT=800
SCALE_FACTOR=200

ORIGIN_OFFSET=WIDTH/2

#using the imported main.py use the line class to create a line class to be drawn in pygame
class Line(Line):
    #this is the constructor for the line class
    def __init__(self, p1, p2):
        #call the parent constructor

        super().__init__(p1 , p2)
        #set the color to be drawn
        self.color = (0,0,0)
        #set the width of the line
        self.width = 1

    #this function will draw the line to the screen
    def draw(self):
        pygame.draw.line(screen, self.color, (self.p1.x * SCALE_FACTOR + ORIGIN_OFFSET, self.p1.y * -SCALE_FACTOR + ORIGIN_OFFSET), (self.p2.x * SCALE_FACTOR + ORIGIN_OFFSET, self.p2.y * -SCALE_FACTOR + ORIGIN_OFFSET), self.width)

        #draw circle at the start of the line
        pygame.draw.circle(screen, (255,0,0), (self.p1.x * SCALE_FACTOR + ORIGIN_OFFSET, self.p1.y * -SCALE_FACTOR + ORIGIN_OFFSET), 5)
        
        
        
#list of all currentely displayed lines
lines = []    

#our special points
p1 = Point(0.75,0.1)
p2 = Point(0.5,0.5)
p3 = Point(0.2,0.6)  

#our special lines
l1 = Line(Point(0,0), Point(0.75,0.1))
l1.set_angle(math.radians(-60),True)


print(l1.toString())

lines.append(l1)


# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])

def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


#draw some dotted lines to represent the origin and the x and y axis
for i in range(0,WIDTH,10):
    pygame.draw.line(screen, (0,0,0), (i, 0), (i, HEIGHT), 1)
    pygame.draw.line(screen, (0,0,0), (0, i), (WIDTH, i), 1)

while not quit():
    screen.fill((255, 255, 255))
                    
    for line in lines:
        line.draw()
        
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()