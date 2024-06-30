# Como digitar com PyAutoGui

import pyautogui
import pyperclip # biblioteca necessária para digitar caracteres especiais
# funções de copia e cola

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')
    
'''
Passo a passo:
1 - mover o mouse até a caixa de texto
2 - clicar
3 - escrever
4 - enviar a mensagem
'''

# 1 e 2
pyautogui.click(x = 664, y = 993, duration= 2)

#3
# No comando abaixo usei caractere especial. Ele não será digitado.
# pyautogui.typewrite('Olá, bom dia!')

escrever_frase('Olá, bom dia')

#4

pyautogui.click(x = 910, y = 989, duration = 1)