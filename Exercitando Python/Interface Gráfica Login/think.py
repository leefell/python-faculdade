from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario',size=(20,1))],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*',size=(20,1))],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')],
]

# Janela
janela = sg.Window('Tela de Login', layout)

# Ler os Eventos
while True:
    eventos, valores = janela.read() #unpacking
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'alexandre' and valores['senha'] == '12345':
            print("Bem-vindo Ao Seu EMAIL!")
