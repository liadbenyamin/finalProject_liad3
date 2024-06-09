import pygame
import sys

import main


class Win:
    WIDTH = 1792
    HEIGHT = 1024

    def __init__(self):
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("My Game")
        background = pygame.image.load("res/HP3.png").convert_alpha()
        clock = pygame.time.Clock()
        my_font = pygame.font.SysFont('Comic Sans MS', 100)
        text = my_font.render("You won :D", False, (0, 0, 0))
        my_font2 = pygame.font.SysFont('Comic Sans MS', 50)
        text2 = my_font2.render("Good job!", False, (0, 0, 0))
        btn_text = my_font2.render("Play", False, (0, 0, 0))

        pygame.init()

        while True:
            screen.fill((255, 255, 255))
            screen.blit(background, (0, 0))
            screen.blit(text, (self.WIDTH // 2 - 200, self.HEIGHT // 2 - 300))
            screen.blit(text2, (self.WIDTH // 2 - 450, self.HEIGHT // 2))

            # pygame.draw.rect(screen, (0, 0, ), ())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    pressed = pygame.key.get_pressed()

                    if pressed[pygame.K_SPACE]:
                        exit()

            pygame.display.update()
            clock.tick(60)


class Dead:
    WIDTH = 1792
    HEIGHT = 1024

    def __init__(self):
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("My Game")
        background = pygame.image.load("res/HP3.png").convert_alpha()
        clock = pygame.time.Clock()
        my_font = pygame.font.SysFont('Comic Sans MS', 100)
        text = my_font.render("You lost :(", False, (0, 0, 0))
        my_font2 = pygame.font.SysFont('Comic Sans MS', 50)
        text2 = my_font2.render("Better luck next time!", False, (0, 0, 0))
        btn_text = my_font2.render("Play", False, (0, 0, 0))

        pygame.init()

        while True:
            screen.fill((255, 255, 255))
            screen.blit(background, (0, 0))
            screen.blit(text, (self.WIDTH // 2 - 200, self.HEIGHT // 2 - 300))
            screen.blit(text2, (self.WIDTH // 2 - 450, self.HEIGHT // 2))

            # pygame.draw.rect(screen, (0, 0, ), ())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    pressed = pygame.key.get_pressed()

                    if pressed[pygame.K_SPACE]:
                        exit()

            pygame.display.update()
            clock.tick(60)
