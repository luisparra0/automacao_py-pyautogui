# Como fazer reconhecimento de imagem com pyautogui

import pyautogui

# pyautogui.localteOnScreen('nome do arquivo') 
# como resultado ele da ma caixa de informação com as coordenadas, e o tamanho da imagem

# para encontrar a coordenada do centro de uma imagem
#pyautogui.locateCenterOnScreen('') com isso é encontrado a localização central da imagem


# exemplo prático.

'''
Vamos supor que temos que clicar no quadrado de "não sou um robo" 
'''

#captcha = pyautogui.locateCenterOnScreen('google.png')
#pyautogui.click(captcha[0], captcha[1], duration = 2)

#nesse click captcha[0] é a coordenada x do locateCenterOnScreen e
#captcha[1], coordenada y