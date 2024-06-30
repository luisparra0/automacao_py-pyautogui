#Criar um programa que pede o usuário e senha, e na sequência, copia e
#cola o usuário e senha dentro de um bloco de notas


import pyautogui
import pyperclip
from time import sleep

'''
1- pedir email
2- pedir senha
3- abrir o bloco de notas
4- colar usuario 
5- colar senha
'''
def copiando_colando(texto):
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')

#1
email = pyautogui.prompt(text = 'Digite seu email:', title = 'Email')

#2
senha = pyautogui.password(text = 'Digite sua senha:', title = 'Senha', mask = '-')

#3
pyautogui.click(x = 707, y = 1054, duration= 2)
sleep(1)
pyautogui.typewrite('Bloco de notas')
pyautogui.hotkey('enter')

#4
pyautogui.click(x= 1523,y= 256, duration= 2)
copiando_colando(email)
pyautogui.hotkey('enter')
copiando_colando(senha)