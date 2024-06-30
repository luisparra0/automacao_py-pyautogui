'''
Criar um programa que vai até meu bloco de notas e escreva a seguinte frase: Automação é incrível!
'''
import pyautogui
import pyperclip


'''
1- clicar em pesquisar
2- digitar 'bloco de notas'
3- clicar no aplicativo
4- mover o mouse para a caixa de texto e clicar
5- escrever 'Automação é incrível!' // por ter caracteres especiais vou criar uma função com pyperclip
'''
def escrever (frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')


#1 usando mouseInfo para pegar as coordenadas
pyautogui.click(x = 712, y = 1049, duration= 1)

#2
pyautogui.typewrite('Bloco de notas')

#3
pyautogui.click(x = 755 , y = 256, duration= 1)

#4
pyautogui.click(x = 215,y = 301, duration= 3)

#5
escrever('Automação é incrível!')
