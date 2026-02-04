# import pygame, sys
# from pygame.locals import QUIT

# pygame.init()
# screen = pygame.display.set_mode((600, 600))
# pygame.display.set_caption('Hello World!')
# #Colors
# black = (0,0,0)
# white = (255,255,255)
# red = (255,0,0)
# green = (0,255,0)
# blue = (0,0,255)
# #screen fil
# screen.fill("white")
# pygame.display.update()
# while True:
#    #creating a Rectangle class
#    class Rect():
#        def __init__(self,color,dimensions):
#            self.rect_surf = screen
#            self.rect_color = color
#            self.rect_dimensions=dimensions

#        def draw(self):
#            self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)

#    #creating Instances    

#    greenRect=Rect(green,(50,20,100,100))
#    redRect=Rect(red,(150,200,150,150))
#    blueRect=Rect(blue,(300,400,200,200))
#    #accessing methods 
#    greenRect.draw()
#    blueRect.draw()
#    redRect.draw()
#    for event in pygame.event.get():
#        if event.type == QUIT:
#            pygame.quit()
#            sys.exit()
#    pygame.display.update()





# import pygame,sys
# from pygame.locals import QUIT


# pygame.init()

# screen= pygame.display.set_mode((500,500))
# pygame.display.set_caption("My Screen")

# screen.fill("blue")

# img = pygame.image.load("car.jpg")
# img = pygame.transform.scale(img,(150,150))
# img = pygame.transform.rotate(img,180)
# font=pygame.font.SysFont("Times New Roman",72)
# text=font.render("My Car",True,(0,255,0))
# while True:
#      screen.blit(img,(100,100))
#      screen.blit(text,(0,120))
#      for event in pygame.event.get():
#        if event.type == QUIT:
#            pygame.quit()
#            sys.exit()
#      pygame.display.update()





import pygame,sys
from pygame.locals import QUIT


pygame.init()

screen= pygame.display.set_mode((500,500))
pygame.display.set_caption("My Screen")

screen.fill("blue")

rectangle =pygame. Rect(100,100,50,75)
while True:
    # screen.blit(img,(100,100))
    # screen.blit(text,(0,120))
    
     pygame.draw.rect(screen,"red",rectangle,5)
     for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
     pygame.display.update()