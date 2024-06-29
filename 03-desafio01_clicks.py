'''
Nesse desafio eu devo criar uma nova pasta no meu explorador de arquivos
'''

import pyautogui

#movendo o mouse para a pagina aberta do explorador de arquivos
pyautogui.moveTo(-1345,500, duration= 2)
pyautogui.rightClick()
pyautogui.moveTo(-1179, 398, duration= 1)
pyautogui.click()
pyautogui.click(x= -925, y= -55, duration= 2)