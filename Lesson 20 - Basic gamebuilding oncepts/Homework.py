import pygame

# Initialize pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("My first game screen")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RECT_COLOR = (0, 128, 255)

rect_width, rect_height = 200, 100
rect_x = (640 - rect_width) // 2
rect_y = (480 - rect_height) // 2
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

font = pygame.font.SysFont(None, 36)
text = font.render("My name is Anaira", True, BLACK)
text_rect = text.get_rect(center=(320, 50))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw rectangle
    pygame.draw.rect(screen, RECT_COLOR, rectangle)

    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()