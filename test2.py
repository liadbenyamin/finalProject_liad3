from PIL import Image
import numpy as np

def map_array():
    image = Image.open("MAP1.png")
    input_array = np.asarray(image)
    return input_array

def isCollide(dir, color):

    if dir == "UP":

        pass
    elif dir == "DOWN":

        pass
    elif dir == "RIGHT":

        pass
    elif dir == "LEFT":

        pass


    return False
