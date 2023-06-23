# not by me

import pyautogui
import discord
import os

def screenshot():
    print("Taking screenshot...")
    image = pyautogui.screenshot()
    image.save("screenshot.png") 
    print("Screenshot saved.") 
#insert send screenshot script or something
    os.remove("screenshot.png") 

screenshot()
