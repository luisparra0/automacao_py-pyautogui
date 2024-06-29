# Como pegar e 'arrastar' algo para outro lugar

import pyautogui

'''
Passo a passo:
1 - mover até uma coordenada
2 - clicar 
3 - arrastar até o destino desejado
4 - soltar
'''


for i in range(5):
    #1
    pyautogui.moveTo(-1931,-61, duration= 1)

    #2, 3 e 4) vamos usar a função dragTo. Nela já é feito o clicar e arrastar.
    #No entanto é necessário definir o botão que vai ser feito o click

    pyautogui.dragTo(-101,538, button= 'left', duration= 2)