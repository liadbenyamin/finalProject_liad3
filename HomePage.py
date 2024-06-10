import pygame
import sys

import main

pygame.init()

WIDTH = 1792
HEIGHT = 1024
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Runner in Space")
background = pygame.image.load("res/xaxa.png").convert_alpha()
clock = pygame.time.Clock()
my_font = pygame.font.SysFont('Comic Sans MS', 100)
text = my_font.render("The Runner in Space", True, (0, 0, 0), (255, 255, 255))
my_font2 = pygame.font.SysFont('Comic Sans MS', 50)
text2 = my_font2.render("Hi welcome to my game", True, (0, 0, 0), (255, 255, 255))
text3 = my_font2.render("To start the game please press space", True, (0, 0, 0), (255, 255 ,255))
btn_text = my_font2.render("Play", True, (0, 0, 0))

r_wi = WIDTH / 1.75
r_he = HEIGHT / 2

while True:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    rect = pygame.rect.Rect(WIDTH // 2 - r_wi // 2, HEIGHT // 2 - r_he // 2, r_wi, r_he - 10)
    pygame.draw.rect(screen, (128, 128, 128), rect)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 - 150))
    screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2 - text2.get_height() // 2))
    screen.blit(text3, (WIDTH // 2 - text3.get_width() // 2, HEIGHT // 2 - text3.get_height() // 2 + 150))

    # pygame.draw.rect(screen, (0, 0, ), ())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_SPACE]:
                game = main.Game()

    pygame.display.update()
    clock.tick(60)
