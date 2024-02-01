import socket
import threading

import pygame
import sys
import numpy

pygame.init()
background = pygame.image.load("MAP1.png")
screen = pygame.display.set_mode([1792,1024])
clock = pygame.time.Clock()
pygame.display.set_caption("pygame test1")

s = socket.socket()
s.connect(('127.0.0.1', 9999))
color_msg = s.recv(1024).decode()


def handle_connection():
    while True:
        msg = s.recv(1024).decode()
        print(msg)

def is_not_black(direction):
    if direction == 'RIGHT':
        # color_up = screen.get_at((character.x + width+1, character.y))
        # color_down = screen.get_at((character.x + width+1, character.y+height+1))
        color_up = screen.get_at((character.x + width + 1, character.y))
        color_down = screen.get_at((character.x + width + 1, character.y + height + 1))
        return (color_up[0] > 10 or color_up[1] > 10 or color_up[2] > 10) and (color_down[0] > 10 or color_down[1] > 10 or color_down[2] > 10)

    if direction == 'LEFT':
        color_up = screen.get_at((character.x - 1, character.y))
        color_down = screen.get_at((character.x -1, character.y + height + 1))

        return (color_up[0] > 10 or color_up[1] > 10 or color_up[2] > 10) and (color_down[0] > 10 or color_down[1] > 10 or color_down[2] > 10)

    if direction == 'UP':
        color_left = screen.get_at((character.x , character.y-1 ))
        color_right = screen.get_at((character.x + width + 1, character.y - 1))

        return (color_left[0] > 10 or color_left[1] > 10 or color_left[2] > 10) and (color_right[0] > 10 or color_right[1] > 10 or color_right[2] > 10)


    if direction == 'DOWN':
        color_left = screen.get_at((character.x , character.y+height+1 ))
        color_right = screen.get_at((character.x + width + 1, character.y + height+1))

        return (color_left[0] > 10 or color_left[1] > 10 or color_left[2] > 10) and (color_right[0] > 10 or color_right[1] > 10 or color_right[2] > 10)




    # if direction == 'LEFT':
    #     color = screen.get_at((character.x -1 , character.y))
    #     print(color)
    #     return color[0] > 10 or color[1] > 10 or color[2] > 10
    #
    # if direction == 'UP':
    #     color = screen.get_at((character.x , character.y+1))
    #     print(color)
    #     return color[0] > 10 or color[1] > 10 or color[2] > 10
    #
    # if direction == 'DOWN':
    #     color = screen.get_at((character.x , character.y + height))
    #     print(color)
    #     return color[0] > 10 or color[1] > 10 or color[2] > 10


def draw(col):
    if col == 1:
        tup = (255, 0, 0)
    elif col == 2:
        tup = (0, 255, 0)
    else:
        tup = (0, 0, 255)

    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, tup, (x, y, width, height))
    # pygame.draw.rect(screen, (0,0,0), left_wall, 0)
    # pygame.draw.rect(screen, (0,0,0), right_wall, 0)
    pygame.display.update()

x = screen.get_width()//2
y = screen.get_height()//2
speed = 3
width = 40
height = 40

left_wall = pygame.Rect(-2,0,2,600)
right_wall = pygame.Rect(1201,0,2,600)

thread = threading.Thread(target=handle_connection)
thread.start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    character = pygame.Rect(x,y,width, height)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] or pressed[pygame.K_w] and is_not_black('UP'):
        y -= speed
    if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and is_not_black('RIGHT'):
        x += speed
    if pressed[pygame.K_DOWN] or pressed[pygame.K_s] and is_not_black('DOWN'):
        y += speed
    if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and is_not_black('LEFT'):
        x -= speed

    s.send("pressUP".encode())

    draw(int(color_msg))
    clock.tick(60)