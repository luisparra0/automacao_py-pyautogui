import pyautogui
from time import sleep

# Encontrar a posição de algo - usar o mouseInfo
# Fazer algo com essa posição
'''
pyautogui.moveTo(1829,65, duration = 1.5) # Move o cursor do mouse para um ponto da tela.
pyautogui.move(0,100, duration = 2) # Move o cursos do mouse em relação a posição atual
pyautogui.move(0, -150, duration = 1)
pyautogui.click() # Efetua o ato de clicar do mouse

'''

#código abaixo usado para zerar um jogo que o objetivo é apenas dar inúmeros clicks na tela.
# https://www.crazygames.com/game/doge-miner-2
pyautogui.moveTo(-1409,38, duration= 1)
for i in range(1000):
    sleep(0.1) #usando o sleep controlo o tempo das clicadas
    pyautogui.click()