import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Custom Event Example")

sprite1 = pygame.Rect(150, 150, 100, 100)
sprite2 = pygame.Rect(350, 150, 100, 100)

color1 = (255, 0, 0)
color2 = (0, 0, 255)

def change_color():
    global color1, color2
    color1 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    color2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                change_color()

    pygame.draw.rect(screen, color1, sprite1)
    pygame.draw.rect(screen, color2, sprite2)

    pygame.display.update()

pygame.quit()