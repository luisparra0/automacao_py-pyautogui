#Como usar botões e atalhos do teclado


import pyautogui


# para ver todos os nomes de teclas em inglês:
# print(pyautogui.KEYBOARD_KEYS)



# como usar combinações de tecla:
# selecionando um texto e copiando ele :

pyautogui.keyDown('ctrl') #keyDown (pressiona a tecla)
pyautogui.keyDown('a') 
pyautogui.keyUp('ctrl')#keyUp (solta a tecla)
pyautogui.keyUp('a') 
pyautogui.keyDown('ctrl') 
pyautogui.keyDown('c') 
pyautogui.keyUp('ctrl') 
pyautogui.keyUp('c') 

#agora uma forma mais simples:

pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')