import pygame
from random import randint
pygame.init()
screen= pygame.display.set_mode((600,600))
screen.fill((255,255,255))
pygame.display.update()
subway_surfer=pygame.image.load("subwaysurfer.png")
ludo=pygame.image.load("ludo.png")
#ludo = pygame.transform.scale(ludo,(100,100))
templerun=pygame.image.load("templerun.png")
candycrush=pygame.image.load("candycrush.jpg")
screen.blit(subway_surfer,(150,100))
screen.blit(ludo,(150,200))
screen.blit(templerun,(150,300))
screen.blit(candycrush,(150,400))
font=pygame.font.SysFont("Times New Roman",36)
text=font.render("Ludo",True,(0,0,0))
text1=font.render("candycush",True,(0,0,0))
text2=font.render("Subway Surfer",True,(0,0,0))
text3=font.render("Temple run",True,(0,0,0))
screen.blit(text,(350,100))
screen.blit(text1,(350,200))
screen.blit(text2,(350,300))
screen.blit(text3,(350,400))
pygame.display.update()
r= randint(0,255)
g=randint(0,255)
b=randint(0,255)
clr=(r,g,b)
while 1:
    
    event = pygame.event.poll()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)
    if event.type == pygame.MOUSEBUTTONDOWN:
         pos = pygame.mouse.get_pos()
         pygame.draw.circle(screen, 
           ((clr)) ,(pos), 20, 0)
         pygame. display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
         pos2 = pygame.mouse.get_pos()
         pygame.draw.line(screen,((clr)), (pos), (pos2),5)
         pygame.draw.circle(screen, 
           ((clr)) ,(pos2), 20, 0)
         pygame.display.update()


