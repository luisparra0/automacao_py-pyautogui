import pyautogui
import keyboard
from time import sleep
import win32api
import win32con

pyautogui.click(1120,500,duration=1) # Start 

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.06)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while keyboard.is_pressed('1') == False:
        if pyautogui.pixelMatchesColor(1300,534,(0, 0, 0)):
            click(1300,534)
        if pyautogui.pixelMatchesColor(1394,525,(0, 0, 0)):
            click(1394,525)
        if pyautogui.pixelMatchesColor(1478,527,(0, 0, 0)):
            click(1478,527)
        if pyautogui.pixelMatchesColor(1558,527,(0, 0, 0)):
            click(1558,527)