import PySimpleGUI as sg
import string 
import random

layout = [
            [sg.T('Sopa de Letras')]
         ]
num_row = 0

print(string.ascii_lowercase)

for i in string.ascii_lowercase:
    fila = [sg.T(i, size=(7,2), background_color='white', pad=(0.5,0.5), justification='center', key=i + str(num_row), click_submits=True) for i in string.ascii_lowercase]
    layout.append(fila)
    num_row += 1

window = sg.Window('Juego Educativo', grab_anywhere=True).Layout(layout)

while True:
    event, values = window.Read()

    if 'h' in event:
        window.FindElement(event).Update(background_color='red')

