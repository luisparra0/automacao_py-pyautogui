import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(1263,877, (0,152,0), tolerance= 10):
        pyautogui.press('a')
        sleep(0.001)
        
    if pyautogui.pixelMatchesColor(1377,871, (255,0,0)):
        pyautogui.press('s')
        sleep(0.001)
        
    if pyautogui.pixelMatchesColor(1485,872, (244,244,2)):
        pyautogui.press('j')
        sleep(0.001)
        