import PySimpleGUI as sg
from jugar import jugar
from configuracion import configuracion
sg.ChangeLookAndFeel('BrownBlue')
layout = [    
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
            button_color=("white","green"), 
            pad=(15,10), 
            border_width=20)],
         ]
#VENTANA PRINCIPAL
window_main = sg.Window("Juego Educativo",size=(290,375), font='Courier').Layout(layout)

while True:
 button, values = window_main.Read()
 if button=="Jugar":
    jugar()
 if button=="Configuracion":
    configuracion()
 if button=="Salir"or values==None:
     exit(19)
    
window_main.Close()
