import os

import pygame
import sys

import main

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Win:
    WIDTH = 1792
    HEIGHT = 1024
    blink = True

    def __init__(self):
        pygame.init()

        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("My Game")
        background = pygame.image.load("res/HP3.png").convert_alpha()
        clock = pygame.time.Clock()
        my_font = pygame.font.SysFont('Comic Sans MS', 100)
        text = my_font.render("You won :D", True, WHITE, BLACK)
        my_font2 = pygame.font.SysFont('Comic Sans MS', 50)
        text2 = my_font2.render("Good job!", True, WHITE, BLACK)
        text3 = my_font2.render("Press space to start a new game", True, WHITE, BLACK)

        pygame.time.set_timer(pygame.USEREVENT, 500)

        while True:
            screen.fill((255, 255, 255))
            screen.blit(background, (0, 0))
            screen.blit(text, (self.WIDTH // 2 - text.get_width() // 2, self.HEIGHT // 2 - 300))
            screen.blit(text2, (self.WIDTH // 2 - text2.get_width() // 2, self.HEIGHT // 2))

            if self.blink:
                screen.blit(text3, (self.WIDTH // 2 - text3.get_width() // 2, self.HEIGHT // 2 + 150))
            # pygame.draw.rect(screen, (0, 0, ), ())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    pressed = pygame.key.get_pressed()

                    if pressed[pygame.K_SPACE]:
                        self.screen = pygame.display.set_mode((1, 1), flags=pygame.HIDDEN)
                        os.system("python HomePage.py")

                elif event.type == pygame.USEREVENT:
                    self.blink = not self.blink

            pygame.display.update()
            clock.tick(60)


class Lose:
    WIDTH = 1792
    HEIGHT = 1024
    blink = True

    def __init__(self):
        pygame.init()

        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("The Runner in Space")
        background = pygame.image.load("res/HP3.png").convert_alpha()
        clock = pygame.time.Clock()
        my_font = pygame.font.SysFont('Comic Sans MS', 100)
        text = my_font.render("You Lost :(", True, WHITE, BLACK)
        my_font2 = pygame.font.SysFont('Comic Sans MS', 50)
        text2 = my_font2.render("Better luck next time", True, WHITE, BLACK)
        text3 = my_font2.render("Press space to start a new game", True, WHITE, BLACK)

        pygame.time.set_timer(pygame.USEREVENT, 500)

        while True:
            screen.fill((255, 255, 255))
            screen.blit(background, (0, 0))
            screen.blit(text, (self.WIDTH // 2 - text.get_width() // 2, self.HEIGHT // 2 - 300))
            screen.blit(text2, (self.WIDTH // 2 - text2.get_width() // 2, self.HEIGHT // 2))

            if self.blink:
                screen.blit(text3, (self.WIDTH // 2 - text3.get_width() // 2, self.HEIGHT // 2 + 150))
            # pygame.draw.rect(screen, (0, 0, ), ())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    pressed = pygame.key.get_pressed()

                    if pressed[pygame.K_SPACE]:
                        os.system("python HomePage.py")
                        self.screen = pygame.display.set_mode((1, 1), flags=pygame.HIDDEN)

                elif event.type == pygame.USEREVENT:
                    self.blink = not self.blink

            pygame.display.update()
            clock.tick(60)


if len(sys.argv) > 1:
    if sys.argv[1] == "win":
        Win()

    elif sys.argv[1] == "lose":
        Lose()