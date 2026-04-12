import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Sprites Example")

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

x1, y1 = 50, 50   
x2, y2 = 300, 200  

speed = 5

while True:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y1 -= speed
    if keys[pygame.K_DOWN]:
        y1 += speed
    if keys[pygame.K_LEFT]:
        x1 -= speed
    if keys[pygame.K_RIGHT]:
        x1 += speed
        
    pygame.draw.rect(screen, blue, (x1, y1, 50, 50))  
    pygame.draw.rect(screen, red, (x2, y2, 50, 50))   

    pygame.display.update()