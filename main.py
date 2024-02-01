import pygame
import sys

# from Character import Character

pygame.init()
background = pygame.image.load("MAP2(1).png")
playerSprite = pygame.image.load("player2.png")
playerSprite = pygame.transform.scale(playerSprite, (20, 44))
screen = pygame.display.set_mode([1792,1024])
clock = pygame.time.Clock()
pygame.display.set_caption("pygame test1")

def is_black(direction):

    if direction == 'LEFT':
        color_up = screen.get_at((character.x - 10, character.y))
        color_down = screen.get_at((character.x - 10, character.y + 44 + 1))
        return (color_up[0] < 5 and color_up[1] < 5 and color_up[2] < 5) or   (color_down[0] < 5 and color_down[1] < 5 and color_down[2] < 5)

    if direction == 'RIGHT':
        color_up = screen.get_at((character.x + 10+1, character.y))
        color_down = screen.get_at((character.x + 10+1, character.y+44+1))
        return (color_up[0] < 5 and color_up[1] < 5 and color_up[2] < 5) or  (color_down[0] < 5 and color_down[1] < 5 and color_down[2] < 5)

    if direction == 'UP':
        color_left = screen.get_at((character.x, character.y - 2))
        color_right = screen.get_at((character.x + 10 + 10, character.y - 2))

        return (color_left[0] < 5 and color_left[1] < 5 and color_left[2] < 5)  or ( color_right[0] < 5 and color_right[1] < 5 and color_right[2] > 10)

    if direction == 'DOWN':
        color_left = screen.get_at((character.x, character.y + 44 + 1))
        color_right = screen.get_at((character.x + 10 - 2, character.y + 44 - 2))
        print("right", color_right)
        print("left", color_left)
        return (color_left[0] < 5 and color_left[1] < 5 and color_left[2] < 5)  or  (color_right[0] < 5 and color_right[1] < 5 and color_right[2] > 10)



def is_not_black(direction):
    if direction == 'RIGHT':
        color_up = screen.get_at((character.x + width+1, character.y))
        color_down = screen.get_at((character.x + width+1, character.y+height+1))
        print("color up", color_up)
        print("color down", color_down)
        return (color_up[0] > 10 or color_up[1] > 10 or color_up[2] > 10) and (color_down[0] > 10 or color_down[1] > 10 or color_down[2] > 10)

    if direction == 'LEFT':
        color_up = screen.get_at((character.x - 5, character.y))
        color_down = screen.get_at((character.x - 5, character.y + 44 + 1))
        print("color up", color_up)
        print("color down", color_down)
        return not (color_up[0] == 0 and color_up[1] == 0 and color_up[2] == 0) and not (color_down[0] == 0 and color_down[1] == 0 and color_down[2] > 0)

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

    character = pygame.Rect(x,y,width, height)
    pressed = pygame.key.get_pressed()
    if (pressed[pygame.K_UP] or pressed[pygame.K_w] ) and not is_black('UP'):
        y -= speed
    if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and not is_black('RIGHT'):
        x += speed
    if (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and not is_black('DOWN'):
        y += speed
    if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and not is_black('LEFT'):
        x -= speed

    draw()
    clock.tick(60)
