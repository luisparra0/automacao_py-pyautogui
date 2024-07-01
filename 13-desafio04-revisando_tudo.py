'''
1) Navegue até o site https://cursoautomacao.netlify.app/
2) Encontre e clique no campo "Digite seu nome" dentro de 
"exemplos Alertas" e digite seu nome
3) Clique em alerta, para gerar a alerta
4) Feche a alerta
5) Suba a página totalmente para cima
6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá 
fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU
"'''

import webbrowser
import pyautogui
from time import sleep

#1
webbrowser.open('https://cursoautomacao.netlify.app/')
sleep(4)

#2
pyautogui.moveTo(x = 1908, y = 228, duration= 1)
pyautogui.dragTo(x = 1908,y = 402, button= 'left', duration= 2)
#clicando em alerta e digitando meu nome
pyautogui.click(x = 1591,y =545, duration= 1)
pyautogui.typewrite('Luis Parra')

#3
pyautogui.click(x= 1473,y= 602, duration= 1)


#4
pyautogui.doubleClick(x= 1181,y= 202, duration= 1)

#5
sleep(1)
for i in range(3):
    pyautogui.hotkey('shift', 'space')
    
#6
sleep(1)
pyautogui.scroll(-400)
'''pyautogui.moveTo(x = 1907, y = 227, duration= 1)
pyautogui.dragTo(x = 1907, y = 633, duration= 1)'''
pyautogui.click(x = 363, y = 609, duration=1)
sleep(0.5)
pyautogui.click(x = 609, y = 609, duration= 1)


#7
pyautogui.alert(text ='VOCÊ TERMINOU!', title = 'FIM', button = 'OK')