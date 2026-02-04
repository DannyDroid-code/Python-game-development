import pygame

pygame.init()
l=500
w=500

screen = pygame.display.set_mode((l,w))
pygame.display.set_caption("Hello Pygame")
screen.fill("blue")

img = pygame.image.load("background.png")
img = pygame.transform.scale(img,(l,w))

img1= pygame.image.load("car.jpg")
img1 = pygame.transform.scale(img1,(100,100))

font=pygame.font.SysFont("Times New Roman",36)
text=font.render("Hello world",True,(0,200,0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(img,(0,0))
    screen.blit(img1,(50,50))
    screen.blit(text,(150,150))

    pygame.display.update()