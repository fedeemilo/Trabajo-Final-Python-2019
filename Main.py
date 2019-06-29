import PySimpleGUI as sg
from jugar import jugar
from configuracion import configuracion
sg.ChangeLookAndFeel('BrownBlue')
layout = [    
          [sg.T('  Sopa de Letras \n     Educativa   ', 
            background_color='lightgreen', 
            text_color='black',
            relief='groove',
            auto_size_text=True,
            size=(29,2),
            font=('Courier', 18, 'bold'))],
          [sg.Button("Jugar",
            size=(20,3),
            button_color=("white","green"), 
            pad=(15,10), 
            border_width=20)],
          [sg.Button("Configuracion",
            size=(20,3),
            button_color=("white","green"), 
            pad=(15,10), 

            border_width=20)],
          [sg.Button("Salir",
            size=(20,3),
            button_color=("white","red"), 
            pad=(15,10), 
            border_width=20)],
         ]
#VENTANA PRINCIPAL
window_main = sg.Window("Juego Educativo",
              size=(320,455), 
              font='Courier', 
              background_color='lightgreen',
              no_titlebar=True,
              grab_anywhere=True).Layout(layout)

while True:
 button, values = window_main.Read()
 if button=="Jugar":
    jugar()
 if button=="Configuracion":
    configuracion()
 if button=="Salir"or values==None:
     exit(19)
    
window_main.Close()
