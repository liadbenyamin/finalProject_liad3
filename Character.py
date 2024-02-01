# import pygame
#
#
# class Character:
#     def __init__(self):
#         self.image = pygame.image.load("standPlayer NO BG.png")
#         # Call the parent class (Sprite) constructor
#         pygame.sprite.Sprite.__init__(self)
#
#         # Create an image of the block, and fill it with a color.
#         # This could also be an image loaded from the disk.
#         self.image = pygame.Surface([50, 50])
#         # self.image.fill(color)
#
#         # Fetch the rectangle object that has the dimensions of the image
#         # Update the position of this object by setting the values of rect.x and rect.y
#         self.rect = self.image.get_rect()
#
#
# c = Character()
# while True:
#     print()