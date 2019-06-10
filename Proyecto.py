import PySimpleGUI as sg
import string 
import random
#------------------------------------------------------------------------------------------------------------------------------------
#Funciones
def sopa():
    layout = [
            [sg.T('Sopa de Letras')]
         ]
    num_row = 0
    for i in string.ascii_lowercase:
     fila = [sg.T(i, size=(7,2), background_color='white', pad=(0.5,0.5), justification='center', key=i + str(num_row), click_submits=True, enable_events=True) for i in string.ascii_lowercase]
     layout.append(fila)
     num_row += 1

    window = sg.Window('Sopa de letras', grab_anywhere=True).Layout(layout)

    while True:
      event, values = window.Read()

      if event == 'm':
        window.FindElement(event).Update(background_color='red')

def configuracion():
 Lista=[]
 color=["red","blue","green","orange","yellow","gray","purple","pink","brown"]
 layout=[
        [sg.Text("Configurar palabras")],
        [sg.Text("Palabra:", size=(6,1)),sg.InputText(key='input')],
        [sg.Listbox(values=(Lista),key="list", size=(50,3))],
        [sg.Submit("Agregar"),sg.Submit("Quitar")],
        [sg.Text("Colores:")],
        [sg.InputCombo((color), size=(20, 1))],#button_color
        [sg.InputCombo((color), size=(20, 1))],#button_color
        [sg.InputCombo((color), size=(20, 1))],#button_color
        [sg.Text("Orientacion:")],
        [sg.InputCombo(("Vertical","Horizontal"), size=(20, 1))],
        [sg.Text("Cantidad de palabras:")],
        [sg.Text("Sustantivos:", size=(15,1)),sg.InputText()],
        [sg.Text("Verbos:", size=(15,1)),sg.InputText()],
        [sg.Text("Adjetivos:", size=(15,1)),sg.InputText()],
        [sg.Submit("Guardar cambios"),sg.Cancel("Volver")],
        ]
 window=sg.Window("Configuracion",size=(500,720)).Layout(layout)
 while True:
  button, values = window.Read()
  if button=="Guardar cambios":
    print("Hacer")
  if button=="Volver"or values==None:
     exit(19)
  if button=="Agregar":
      Lista.append(values['input'])      
      window.FindElement('list').Update(values=(Lista))
      window.FindElement('input').Update('')    
  if button=="Quitar":
      try:
       Lista.remove(values[0])
      except(ValueError):
          sg.PopupError("No se puede quitar la palabra por que no existe en la lista")        
      window.FindElement('list').Update(values=(Lista))
      
 window.Close()

##########################################################################################
#Main
layout=[    
        [sg.Submit("Jugar",size=(20,3),button_color=("white","green"))],
        [sg.Submit("Configuracion",size=(20,3),button_color=("white","green"))],
        [sg.Cancel("Salir",size=(20,3),button_color=("white","green"))],
        ]
window=sg.Window("Juego Educativo",size=(300,300)).Layout(layout)
while True:
 button, values = window.Read()
 if button=="Jugar":
    sopa()
 if button=="Configuracion":
    configuracion()
 if button=="Cancelar"or values==None:
     exit(19)
    
window.Close()







