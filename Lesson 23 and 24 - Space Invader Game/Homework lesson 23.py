import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader - Part 1")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

player_size = 50
player = pygame.Rect(WIDTH//2, HEIGHT-60, player_size, player_size)
player_speed = 5

enemy_size = 40
enemies = []
for i in range(7):
    x = random.randint(0, WIDTH - enemy_size)
    y = random.randint(0, HEIGHT//2)
    enemies.append(pygame.Rect(x, y, enemy_size, enemy_size))

score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player_size:
        player.x += player_speed
    if keys[pygame.K_UP] and player.y > 0:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.y < HEIGHT - player_size:
        player.y += player_speed

    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, WIDTH - enemy_size)
            enemy.y = random.randint(0, HEIGHT//2)

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()