import pygame
import sys

import main

pygame.init()

WIDTH = 1792
HEIGHT = 1024
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
background = pygame.image.load("res/HP3.png").convert_alpha()
clock = pygame.time.Clock()
my_font = pygame.font.SysFont('Comic Sans MS', 100)
text = my_font.render("My Game", False, (0, 0, 0))
my_font2 = pygame.font.SysFont('Comic Sans MS', 50)
text2 = my_font2.render("Welcome to the best game you'll play in your life!", False, (0, 0, 0))
btn_text = my_font2.render("Play", False, (0, 0, 0))

while True:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(text, (WIDTH // 2 - 200, HEIGHT // 2 - 300))
    screen.blit(text2, (WIDTH // 2 - 450, HEIGHT // 2))

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
