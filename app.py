# biblioteca PySimpleGUI
# Apenas a interface Grafica
import PySimpleGUI as sg

sg.theme('Dark Blue 3')

janela_principal = [
    [sg.Text('E-mail'), sg.Input(key='email')],
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*')],
    [sg.FolderBrowse('Escolher pasta anexos', target='input_anexos'),sg.Input(key='input_anexos')],
    [sg.FolderBrowse('Escolher pasta planilha', target='imput_planilha'),sg.Input(key='input_planilha')],
    [sg.Button('Salvar')]
]

janela = sg.Window('Principal', layout=janela_principal)

while True:
    event, values = janela.read()
    if event == sg.CLOSED:
        break
