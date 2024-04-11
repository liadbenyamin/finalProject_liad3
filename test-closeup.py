import pygame as pg, time, random
from pygame.locals import *
from pytmx.util_pygame import load_pygame


def blit_all_tiles(screen, tmxdata, world_offset):
    for layer in tmxdata:
        for tile in layer.tiles():
            # tile[0] = x coordinate
            # tile[1] = y coordinate
            # tile[2] = image data
            x_pixel = tile[0] * 32 + world_offset[0]
            y_pixel = tile[1] * 32 + world_offset[1]
            screen.blit(tile[2], (x_pixel, y_pixel))


    # Game Variables
    def main():
        tmxdata = load_pygame("assets/Chris' adventure.tmx")
        # Standing
        player_stand = pg.image.load("CharAssets/Cris 01.png")
        player_stand = pg.transform.scale(player_stand, (32, 32))
        # Moving Right
        player_left = [
            pg.image.load("CharAssets/Cris 04.png"),
            pg.image.load("CharAssets/Cris 05.png"),
            pg.image.load("CharAssets/Cris 06.png"),
        ]
        player_up = [
            pg.image.load("CharAssets/Cris 07.png"),
            pg.image.load("CharAssets/Cris 08.png"),
            pg.image.load("CharAssets/Cris 09.png"),
        ]
        player_down = [
            pg.image.load("CharAssets/Cris 01.png"),
            pg.image.load("CharAssets/Cris 02.png"),
            pg.image.load("CharAssets/Cris 03.png"),
        ]
# Resize
        player_left = [pg.transform.scale(image, (32, 32)) for image in player_left]
        player_left_f = 0
        player_up = [pg.transform.scale(image, (32, 32)) for image in player_up]
        player_up_f = 0
        player_down = [pg.transform.scale(image, (32, 32)) for image in player_down]
        player_down_f = 0
        # Flipping
        player_right = [pg.transform.flip(image, True, False) for image in player_left]
        player_right_f = 0
        direction = "stand"
        world_offset = [0, 0]

        quit = False
        x = 400
        y = 200 + 128
        # Game Loop
        while not quit:
            screen.fill((0, 0, 0))
            blit_all_tiles(screen, tmxdata, world_offset)
            # Events
            keypressed = pg.key.get_pressed()
            for event in pg.event.get():
                # print(event)
                if event.type == QUIT:
                    quit = True
            if keypressed[ord("a")]:
                x = x - 20
                world_offset[0] += 40
                direction = "left"
            if sum(keypressed) == 0:
                direction = "stand"
            if keypressed[ord("d")]:
                x = x + 20
                world_offset[0] -= 40
                direction = "right"
            if keypressed[ord("w")]:
                y = y - 20
                world_offset[1] += 40
                direction = "up"
            if keypressed[ord("s")]:
                y = y + 20
                world_offset[1] -= 40
                direction = "down"
            if y < 204:
                y = 204
            if y >= screen.get_height() - 204 - 32:
                y = screen.get_height() - 204 - 32
            if x < 204:
                x = 204
                # world_offset[0] += 10
            if x >= screen.get_width() - 204 - 32:
                x = screen.get_width() - 204 - 32

            # Game Logic
            # player = Rect(x, y, 32, 32)
            # pg.draw.rect(screen, (225, 0, 120), player)
            if direction == "stand":
                screen.blit(player_stand, (x, y))
            elif direction == "left":
                screen.blit(player_left[player_left_f], (x, y))
                player_left_f = (player_left_f + 1) % len(player_left)
            elif direction == "right":
                screen.blit(player_right[player_right_f], (x, y))
                player_right_f = (player_right_f + 1) % len(player_right)
            elif direction == "up":
                screen.blit(player_up[player_up_f], (x, y))
                player_up_f = (player_up_f + 1) % len(player_up)
            elif direction == "down":
                screen.blit(player_down[player_down_f], (x, y))
                player_down_f = (player_down_f + 1) % len(player_down)

            # Screen Update
            pg.display.update()
            clock.tick(60)


            # Game Initialization
            if __name__ == "__main__":
                width, height = 800, 600
                pg.init()
                pg.mixer.init()
                screen = pg.display.set_mode((width, height))
                pg.display.set_caption("Chris' quest")
                clock = pg.time.Clock()
                main()
                pg.quit()