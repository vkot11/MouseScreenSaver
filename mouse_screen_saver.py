import pyautogui
import random
import numpy as np
import os

# PRESS CTRL + C in TERMINAL to STOP

pyautogui.FAILSAFE = False

def border_detected(SCREENWIDTH, SCREENHEIGHT, currentMouseX, currentMouseY, next_angle):
    
    currentMouseX, currentMouseY = pyautogui.position()
    
    if currentMouseX == (SCREENWIDTH - 1):
        if next_angle <= 90: 
            next_angle = 180 - next_angle
        else: 
            next_angle = 180 + (360 - next_angle)

    elif currentMouseX == 0:
        if next_angle <= 180: 
            next_angle = 180 - next_angle
        else: 
            next_angle = 270 - next_angle + 270

    elif currentMouseY == 0:
        next_angle = 360 - next_angle

    elif currentMouseY == (SCREENHEIGHT - 1):
        next_angle = 360 - next_angle

    return next_angle


def move_mouse(speed, SCREENWIDTH, SCREENHEIGHT, next_angle):

    currentMouseX, currentMouseY = pyautogui.position()
    next_angle_rad = np.radians(next_angle) 

    # ------------- ONE -------------
    if next_angle <= 90:
        pointX = SCREENWIDTH - 1
        pointY = currentMouseY - (SCREENWIDTH - currentMouseX) * np.tan(next_angle_rad)

        if pointY < 0:
            pointX = currentMouseX + (currentMouseY / np.tan(next_angle_rad))     
            pointY = 0

    # ------------- TWO -------------
    elif next_angle <= 180 and next_angle > 90:
        pointX = currentMouseX + (currentMouseY / np .tan(next_angle_rad))
        pointY = 0

        if pointX < 0:
            pointX = 0    
            pointY = currentMouseY + (currentMouseX * np.tan(next_angle_rad))

    # ------------- THREE -----------
    elif next_angle <= 270 and next_angle > 180:
        pointX = 0
        pointY = currentMouseY + (currentMouseX * np.tan(next_angle_rad))

        if pointY > SCREENHEIGHT - 1:
            pointX = currentMouseX - ((SCREENHEIGHT - (currentMouseY - 1)) / np.tan(next_angle_rad))
            pointY = SCREENHEIGHT - 1

    # ------------- FOUR ------------
    elif next_angle <= 360 and next_angle > 270:
        next_angle -= 270
        next_angle_rad = np.radians(next_angle) 

        pointX = SCREENWIDTH - 1   
        pointY = currentMouseY + ((SCREENWIDTH - 1 - currentMouseX)) / np.tan(next_angle_rad)

        if pointY > SCREENHEIGHT - 1:
            pointX = currentMouseX + ((SCREENHEIGHT - currentMouseY) * np.tan(next_angle_rad))
            pointY = SCREENHEIGHT - 1
        
        next_angle += 270

    # -------- mouse movement speed-------------
    vector_length = np.sqrt((pointX - currentMouseX)**2+(pointY - currentMouseY)**2)
    duration = vector_length // speed

    pyautogui.moveTo(pointX, pointY, duration)

    return next_angle, pointX, pointY


def main():
    SCREENWIDTH, SCREENHEIGHT = pyautogui.size()
    next_angle = random.randrange(0, 360)
    
    os.system("cls")
    print("ScreenSize =", SCREENWIDTH, SCREENHEIGHT)
    print("Random angle:", next_angle)
    print("-"*30)

    while True:
        next_angle, currentMouseX, currentMouseY = move_mouse(550, SCREENWIDTH, SCREENHEIGHT, next_angle)
        next_angle = border_detected(SCREENWIDTH, SCREENHEIGHT, currentMouseX, currentMouseY, next_angle)


if __name__ == "__main__":
    main()