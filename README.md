# MouseScreenSaver
Screen saver where the cursor is used as an object

Overview

This Python script uses the pyautogui library to simulate continuous mouse movement across the screen based on random angles.

Installation
Scripts uses PIL and numpy to generate images.

    pip3 install -r requirements.txt
    
Usage

    Run the script:

    python mouse_movement.py

    Execution:
        Upon running, the script initializes and prints the screen size, a randomly chosen initial movement angle, and begins moving the mouse.
        The mouse will move continuously according to the specified speed (550 pixels per second by default).
        The script handles border detection to ensure the mouse movement stays within screen boundaries.
        To stop the script, manually terminate the process in your terminal or command prompt (Ctrl+C).