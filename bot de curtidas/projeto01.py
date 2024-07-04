import pyautogui
import webbrowser
from time import sleep

while True:
    #1
    webbrowser.open('https://www.instagram.com')
    sleep(1)

    #2 clicando em continuar como (meu login)
    pyautogui.moveTo(1438,591, duration= 2)
    pyautogui.click()
    pyautogui.click(x= 997 , y=364 ,  duration = 1)
    pyautogui.typewrite('nike')
    pyautogui.click(x = 1183, y = 364, duration= 2)
    sleep(0.5)
    pyautogui.click(1153,843, duration= 1)
    try:
        # Tenta localizar a imagem na tela
        coracao = pyautogui.locateCenterOnScreen('locate.png')
        if coracao is not None:
            sleep(86400)
            
        else:
            print("Imagem não encontrada, movendo para a coordenada (1352, 900)")
            pyautogui.moveTo(x=1352, y=900, duration=1)
    except pyautogui.ImageNotFoundException:
            print("Imagem não encontrada, movendo para a coordenada (1352, 900)")
            pyautogui.click(x=1341, y=698, duration=1)
            pyautogui.click(x = 1463, y = 830, duration = 1)
            pyautogui.typewrite('Legal!')
            sleep(1)
            pyautogui.hotkey('enter')
            sleep(86400)   


