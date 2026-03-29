import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")

img = pygame.image.load("image.png")
img = pygame.transform.scale(img, (300, 300))

x = 100
y = 100

running = True
while running:
    screen.fill((58, 58, 58))

    screen.blit(img, (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()