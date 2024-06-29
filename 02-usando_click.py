#como usar a função click

import pyautogui


# Click personalizado:
pyautogui.click(x= 100, y = 100, clicks=1000, interval= 0.1, button= 'left', duration=2)
'''
X e Y são as coordenadas, clicks é a quantidade devezes que irá clicar e interval o intervalo entre os clicks. Button qual o botão do mouse e 
duration qual o tempo para chegar na coordenada do mouse.
'''

# Click na posição atual
pyautogui.click() # como default tem o botão esquerdo
pyautogui.click(button= 'left')
pyautogui.click(button= 'right')
pyautogui.click(button= 'middle')

# Clicar X vezes
pyautogui.click(clicks=10)

# Algumas funções prontas para clicks
pyautogui.doubleClick() #clicks duplos
pyautogui.tripleClick() #clicks triplos
pyautogui.rightClick() #click com o botão direito
pyautogui.middleClick() #click com o botão do meio

