import pygame
import sys
import test2
# from Character import Character

pygame.init()
background = pygame.image.load("MAP1.png")
playerSprite = pygame.image.load("player2.png")
# playerSprite = pygame.transform.scale(playerSprite, (202, 100))
screen = pygame.display.set_mode([1792,1024])
clock = pygame.time.Clock()
pygame.display.set_caption("pygame test1")

map_array = test2.map_array()


def is_not_black(direction):
    if direction == 'RIGHT':
        next_x = character.x + 1 + 66
        next_y = character.y
    elif direction == 'LEFT':
        next_x = character.x - 1
        next_y = character.y
    elif direction == 'UP':
        next_x = character.x
        next_y = character.y - 1
    elif direction == 'DOWN':
        next_x = character.x
        next_y = character.y + 1
    else:
        # Handle invalid direction
        return False

    # Check if the next_x and next_y values are within bounds
    if 0 <= next_x < len(map_array) and 0 <= next_y < len(map_array[0]):
        color_at_next_position = map_array[next_x][next_y]
        color_next_list = color_at_next_position.tolist()
        if color_next_list[0] > 10 or color_next_list[1] > 10 or color_next_list[2] > 10:
            return True

    # Not black
    return False


    # if 0 <= next_x < map_width and 0 <= next_y < map_height:
    #     color_at_next_position = map_array[next_y][next_x]
    #
    #     if color_at_next_position.tolist() != [0, 0, 0, 255]:
    #         return True

    # Not black



def draw():
    screen.blit(background, (0, 0))

    player_center_x = x + playerSprite.get_width() // 2
    player_center_y = y + playerSprite.get_height() // 2

    # myrect = pygame.draw.rect(screen, (0, 0, 255), (player_center_x, player_center_y, width, height))
    rect_x = player_center_x - (width // 2)
    rect_y = player_center_y - (height // 2)
    screen.blit(playerSprite, (rect_x,rect_y))

    # You need to set a pivot to make the image go to center
    # you could do it to the image or create the image before and set the rect to the center to make sure you have
    # collision box which works good with the player sprite.


    # pygame.draw.rect(screen, (0,0,0), left_wall, 0)
    # pygame.draw.rect(screen, (0,0,0), right_wall, 0)
    pygame.display.update()

x = screen.get_width()//2
y = screen.get_height()//2
speed = 1
# cube size
width = 40
height = 40

left_wall = pygame.Rect(-2,0,2,600)
right_wall = pygame.Rect(1201,0,2,600)
# char1 = Character()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    character = pygame.Rect(x,y,80, 66)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] or pressed[pygame.K_w] and is_not_black('UP'):
        y -= speed
    if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and is_not_black('RIGHT'):
        x += speed
    if pressed[pygame.K_DOWN] or pressed[pygame.K_s] and is_not_black('DOWN'):
        y += speed
    if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and is_not_black('LEFT'):
        x -= speed

    draw()
    clock.tick(60)
