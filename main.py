import json
import math
import os
import socket
import threading
from time import sleep

import pygame


class Game:
    soc = None
    background = None
    WIDTH = 20
    HEIGHT = 40
    imposterSprite = None
    runnerSprite = None
    playerFocus = None
    screen = None
    clock = None

    KILL_RADIUS = 75
    spawn_second_sprite = False
    second_sprite_x = 0
    second_sprite_y = 0
    role = ""
    startFocus = False
    timer = 1000
    x = 0
    y = 0

    # Fonts
    roleHeaderFont = None

    running = True
    socketConnected = False

    def __init__(self):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.connect(("127.0.0.1", 9999))
        self.background = pygame.image.load("res/MAP2(1).png")
        self.imposterSprite = pygame.image.load("res/player1.png")
        self.imposterSprite = pygame.transform.scale(self.imposterSprite, (self.WIDTH, self.HEIGHT))
        self.runnerSprite = pygame.image.load("res/player2.png")
        self.runnerSprite = pygame.transform.scale(self.runnerSprite, (self.WIDTH, self.HEIGHT))
        self.playerFocus = pygame.image.load("res/playerFocus.png")
        self.screen = pygame.display.set_mode([1800, 1028])
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("pygame test1")
        self.roleHeaderFont = pygame.font.SysFont("Arial", 25)
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.x = self.screen.get_width() // 2
        self.y = self.screen.get_height() // 2
        speed = 2

        self.socketConnected = True
        thread = threading.Thread(target=self.thread_listener)
        thread.start()

        # left_wall = pygame.Rect(-2, 0, 2, 600)
        # right_wall = pygame.Rect(1201, 0, 2, 600)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.event.get()
                    pygame.quit()

                elif event.type == pygame.USEREVENT and self.startFocus:
                    if self.timer > 0:
                        self.timer -= 1
                    else:
                        self.startFocus = False
                        self.screen = pygame.display.set_mode((1, 1), flags=pygame.HIDDEN)

                        if self.role == 'imposter':
                            os.system("python EndScreens.py lose")
                        else:
                            os.system("python EndScreens.py win")

                        if self.socketConnected:
                            self.soc.sendall(json.dumps({"type": "reset"}).encode())
                            self.soc.close()
                            self.socketConnected = False

            self.character = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)
            pressed = pygame.key.get_pressed()
            if (pressed[pygame.K_UP] or pressed[pygame.K_w]) and not self.is_black('UP'):
                self.y -= speed
                obj = json.dumps({"type": "pos_update", "x": self.character.x, "y": self.character.y, "player": 1})
                self.soc.sendall(obj.encode())
                sleep(.005)
                self.startFocus = True

            if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and not self.is_black('RIGHT'):
                self.x += speed
                obj = json.dumps({"type": "pos_update", "x": self.character.x, "y": self.character.y, "player": 1})
                self.soc.sendall(obj.encode())
                sleep(.005)
                self.startFocus = True

            if (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and not self.is_black('DOWN'):
                self.y += speed
                obj = json.dumps({"type": "pos_update", "x": self.character.x, "y": self.character.y, "player": 1})
                self.soc.sendall(obj.encode())
                sleep(.005)
                self.startFocus = True

            if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and not self.is_black('LEFT'):
                self.x -= speed
                obj = json.dumps({"type": "pos_update", "x": self.character.x, "y": self.character.y, "player": 1})
                self.soc.sendall(obj.encode())
                sleep(.005)
                self.startFocus = True

            if pressed[pygame.K_SPACE] and self.role == "imposter":
                self.dist = math.sqrt((self.second_sprite_x - self.character.x) ** 2 + (self.second_sprite_y - self.character.y) ** 2)
                print(f"DIST: {self.dist} ({'NOT ' if self.dist > self.KILL_RADIUS else ''}IN RADIUS)")
                if self.dist <= self.KILL_RADIUS:
                    obj = json.dumps({"type": "kill"})
                    self.soc.sendall(obj.encode())
                    self.spawn_second_sprite = False
                    self.screen = pygame.display.set_mode((1, 1), flags=pygame.HIDDEN)
                    os.system("python EndScreens.py win")
                    self.socketConnected = False
                    if self.socketConnected:
                        self.soc.sendall(json.dumps({"type": "reset"}).encode())
                        self.soc.close()

            if not self.startFocus and pressed and self.role == "runner":
                obj = json.dumps({"type": "start_focus"})
                self.soc.sendall(obj.encode())
                self.startFocus = True

            self.draw()
            self.clock.tick(60)

    def thread_listener(self):
        while self.socketConnected:
            data = self.soc.recv(1024).decode()
            print(data)

            if data.count("}") == 1:
                obj = json.loads(data)
                if 'type' in obj:
                    if obj['type'] == "spawn_sprites":
                        self.spawn_second_sprite = True
                        self.socketConnected = True
                    elif obj['type'] == "pos_update":
                        self.second_sprite_x = obj['x']
                        self.second_sprite_y = obj['y']
                        print(self.second_sprite_x)
                        print(self.second_sprite_y)

                    elif obj['type'] == 'kill':
                        self.screen = pygame.display.set_mode((1, 1), flags=pygame.HIDDEN)
                        os.system("python EndScreens.py lose")
                        self.socketConnected = False
                        if self.socketConnected:
                            self.soc.sendall(json.dumps({"type": "reset"}).encode())
                            self.soc.close()

                    elif obj['type'] == "role" and self.role == "":
                        self.role = obj['role']
                        print(self.role)
                    elif obj['type'] == "start_focus":
                        self.startFocus = True
            else:
                data = data.split("{")[-1]
                obj = json.loads(data)
                if 'type' in obj:
                    if obj['type'] == "spawn_sprites":
                        self.spawn_second_sprite = True

                    elif obj['type'] == "pos_update":
                        self.second_sprite_x = obj['x']
                        self.second_sprite_y = obj['y']
                        print(self.second_sprite_x)
                        print(self.second_sprite_y)

                    elif obj['type'] == 'kill':
                        self.screen = pygame.display.set_mode((1, 1), flags=pygame.HIDDEN)
                        os.system("python EndScreens.py lose")
                        self.socketConnected = False
                        if self.socketConnected:
                            self.soc.sendall(json.dumps({"type": "reset"}).encode())
                            self.soc.close()
                    #
                    # elif obj['type'] == 'win':
                    #     self.screen = pygame.display.set_mode((1, 1), flags=pygame.HIDDEN)
                    #     os.system("python EndScreens.py lose")
                    #     if self.socketConnected:
                    #         self.soc.sendall(json.dumps({"type": "reset"}).encode())
                    #         self.soc.close()
                    #         self.socketConnected = False

                        self.socketConnected = False
                        self.screen = pygame.display.set_mode((1, 1), flags=pygame.HIDDEN)
                        os.system("python EndScreens.py lose")
                        pygame.quit()

                    elif obj['type'] == "role" and self.role == "":
                        self.role = obj['role']
                        print(self.role)

                    elif obj['type'] == "start_focus":
                        self.startFocus = True

    def is_black(self, direction):

        if direction == 'LEFT':
            color_up = self.screen.get_at((self.character.x - 10, self.character.y))
            color_down = self.screen.get_at((self.character.x - 10, self.character.y + 40 + 1))
            return ((color_up[0] < 5 and color_up[1] < 5 and color_up[2] < 5)
                    or (color_down[0] < 5 and color_down[1] < 5 and color_down[2] < 5))

        if direction == 'RIGHT':
            color_up = self.screen.get_at((self.character.x + 10 + 1, self.character.y))
            color_down = self.screen.get_at((self.character.x + 10 + 1, self.character.y + 40 + 1))
            return ((color_up[0] < 5 and color_up[1] < 5 and color_up[2] < 5)
                    or (color_down[0] < 5 and color_down[1] < 5 and color_down[2] < 5))

        if direction == 'UP':
            color_left = self.screen.get_at((self.character.x, self.character.y - 2))
            color_right = self.screen.get_at((self.character.x + 10 + 10, self.character.y - 2))

            return ((color_left[0] < 5 and color_left[1] < 5 and color_left[2] < 5)
                    or (color_right[0] < 5 and color_right[1] < 5 and color_right[2] > 10))

        if direction == 'DOWN':
            color_left = self.screen.get_at((self.character.x, self.character.y + 40 + 1))
            color_right = self.screen.get_at((self.character.x + 10 - 2, self.character.y + 44 - 2))

            return ((color_left[0] < 5 and color_left[1] < 5 and color_left[2] < 5)
                    or (color_right[0] < 5 and color_right[1] < 5 and color_right[2] > 10))

    def draw(self):

        self.screen.blit(self.background, (0, 0))

        player_center_x = self.x + self.runnerSprite.get_width() // 2
        player_center_y = self.y + self.runnerSprite.get_height() // 2

        rect_x = player_center_x - (self.WIDTH // 2) - 10
        rect_y = player_center_y - (self.HEIGHT // 2)

        if self.role == "imposter":
            self.screen.blit(self.imposterSprite, (rect_x, rect_y))
            if self.spawn_second_sprite:
                self.screen.blit(self.runnerSprite, (self.second_sprite_x - 10, self.second_sprite_y))
        else:
            self.screen.blit(self.runnerSprite, (rect_x, rect_y))
            if self.spawn_second_sprite:
                self.screen.blit(self.imposterSprite, (self.second_sprite_x - 10, self.second_sprite_y))

        if self.startFocus:
            self.screen.blit(self.playerFocus, (player_center_x - 1500, player_center_y - 1000))

        roleText = self.roleHeaderFont.render(self.role.capitalize(), True, (0, 0, 0), (255, 255, 255))
        text_rect = roleText.get_rect().center = (self.screen.get_width() // 2 - 30, 10)
        self.screen.blit(roleText, text_rect)

        timerText = self.roleHeaderFont.render(str(self.timer).rjust(3) if self.timer >= 0 else 'nice', True, (0, 0, 0),
                                               (255, 255, 255))
        self.screen.blit(timerText, (10, 10))

        pygame.display.update()


pygame.quit()
