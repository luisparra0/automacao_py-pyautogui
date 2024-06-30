import pyautogui
from time import sleep
#print da tela toda
#pyautogui.screenshot('teste.jpg')


#print de uma parte específica: pyautogui.screenshot('nome.jpg', coordenada inicial, qtd_pixel_direita, qtd_pixel_esquerda)
sleep(3)
pyautogui.screenshot('bloco_de_notas.jpg', region=(1163,296, 553,605))