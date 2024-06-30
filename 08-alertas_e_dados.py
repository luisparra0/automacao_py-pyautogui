# Alertar e pedir informações no PyAutoGui


import pyautogui

# Alertando
# pyautogui.alert(text = 'Iniciando sua automação', title =' Automação de login', button = 'Ok')


# Pedindo informação
#email = pyautogui.prompt(text = 'Digite seu e-mail', title = 'Informação obrigatória')
#print(email)

# Controle de fluxo da automação: 

'''resposta = pyautogui.confirm(text = 'Continuar rodando nossa automação?', title = 'Confirmação',
                  buttons = ['sim', 'não', 'cancelar'])

if resposta == 'sim':
    print('Continuando. . .')
elif resposta == 'não':
    print('Encerrando. . .')
else:
    print('Cancelando. . .')'''
    
senha = pyautogui.password(text = 'Digite sua senha', title = 'dados de login', mask ='-')
print(senha)