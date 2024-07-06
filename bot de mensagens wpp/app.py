import pyautogui
from time import sleep
import webbrowser


telefones = {'xxxxxxxxx', 'xxxxxxxxx'}

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(620,260, duration= 1)
    sleep(10)
    pyautogui.typewrite('Testando bot de mensagem wpp bb')
    sleep(5)
    pyautogui.press('enter')
    sleep(300)
    
    
# caso eu tenha uma lista txt com os números, posso realizar assim o programa.   
# telefones = []
# with open('fones.txt','r') as arquivo:
#     for linha in arquivo:
#         telefones.append(linha.split('\n'[0]))