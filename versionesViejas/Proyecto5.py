import PySimpleGUI as sg
import string 
import random
import json
#--------------------------------------------------------------------------------------------------------------------
#Funciones
def sopa():
    with open('configuracion.json') as f:
     data = json.load(f)
    layout =[]
    if data["orientacion"]=="Horizontal":
      m=len(data["palabras"])
      n=len(data["palabras"][0])      
    else:
      m=len(data["palabras"][0])
      n=len(data["palabras"])
    for i in range(m):
      layout.append([])
    palabras={}
    if data["orientacion"]=="Horizontal":
     azar=[]
     for i in range(m):
      azar.append(i)
     for f in range(m):
      r=random.choice(azar)
      azar.remove(r)
      word=data["palabras"][r]
      palabras[word]={}
      palabras[word]["tipo"]="segun pattern"
      palabras[word]["coord"]={}
      num=random.randint(0,(n-len(word)))
      for i in range(num):
       layout[f].append(sg.T(random.choice(string.ascii_lowercase), size=(7,2), background_color='green', pad=(0.5,0.5), justification='center', key=i , click_submits=True, enable_events=True))
      for i in range(len(word)):
       layout[f].append(sg.T(word[i], size=(7,2), background_color='green', pad=(0.5,0.5), justification='center', key=i , click_submits=True, enable_events=True))
       palabras[word]["coord"][word[i]]=(f,num+i)
      for i in range(n-len(word)-num):
       layout[f].append(sg.T(random.choice(string.ascii_lowercase), size=(7,2), background_color='green', pad=(0.5,0.5), justification='center', key=i , click_submits=True, enable_events=True))
     return layout 
    else:
     azar=[]
     for i in range(n):
      azar.append(i)
     for f in range(n):
      r=random.choice(azar)
      azar.remove(r)
      word=data["palabras"][r]
      palabras[word]={}
      palabras[word]["tipo"]="segun pattern"
      palabras[word]["coord"]={}
      num=random.randint(0,(m-len(word)))
      for c in range(num):
        layout[c].append(sg.T(random.choice(string.ascii_lowercase), size=(7,2), background_color='green', pad=(0.5,0.5), justification='center', key=i , click_submits=True, enable_events=True))
      for c in range(len(word)):
        layout[c+num].append(sg.T(word[c], size=(7,2), background_color='green', pad=(0.5,0.5), justification='center', key=i , click_submits=True, enable_events=True))
        palabras[word]["coord"][word[c]]=(c+num,f)
      for c in range(num+len(word),m):
        layout[c].append(sg.T(random.choice(string.ascii_lowercase), size=(7,2), background_color='green', pad=(0.5,0.5), justification='center', key=i , click_submits=True, enable_events=True))  
     return layout   
def jugar():
    layout=sopa()
    window = sg.Window('Sopa de letras',size=(1280,720), grab_anywhere=True, font='Courier').Layout(layout)
    while True:
      event, values = window.Read()
      if event == 'm':
        window.FindElement(event).Update(background_color='red')
def configuracion():
 with open('configuracion.json') as f:
     data = json.load(f)
 color=["red","blue","green","orange","yellow","gray","purple","pink","brown"]
 layout=[
        [sg.Text(" Configurar palabras ", relief='raised')],
        [sg.Text("Ingrese una palabra", size=(20,1)), sg.InputText(key='input', size=(20,3))],
        [sg.Listbox(values=(data["palabras"]),key="list", size=(50,3))],
        [sg.Submit("Agregar"),sg.Submit("Quitar")],
        [sg.Text("Colores:")],
        [sg.Text("Sustantivos"),sg.InputCombo((color), size=(5, 1),default_value=data["colores"]["Sustantivos"]),sg.Text("Verbos"),sg.InputCombo((color), size=(5, 1),default_value=data["colores"]["Verbos"]),sg.Text("Adjetivos"),sg.InputCombo((color), size=(5, 1),default_value=data["colores"]["Adjetivos"])],
        [sg.Text("Orientacion:")],
        [sg.InputCombo(("Vertical","Horizontal"), size=(10, 1),default_value=data["orientacion"])],
        [sg.Text("Cantidad de palabras:")],
        [sg.Text("Sustantivos:", size=(12,1)),sg.InputText(size=(3,1),default_text =data["cantidad"]["Sustantivos"]),sg.Text("Verbos:", size=(7,1)),sg.InputText(size=(3,1),default_text =data["cantidad"]["Verbos"]),sg.Text("Adjetivos:", size=(10,1)),sg.InputText(size=(3,1),default_text =data["cantidad"]["Verbos"])],
        [sg.Text("Mayusculas/Minusculas:")],
        [sg.InputCombo(("Mayusculas","Minusculas"), size=(10, 1),default_value=data["mayus"])],
        [sg.Text("Tipografías de títulos y texto para el reporte:")],
        [sg.Text("Titulos:"),sg.InputCombo((color), size=(5, 1),default_value=data["titulos"])],
        [sg.Text("Textos:"),sg.InputCombo((color), size=(5, 1),default_value=data["textos"])],
        [sg.Text("Estilo")],
        [sg.InputCombo(("Vertical","Horizontal"), size=(10, 1),default_value=data["estilo"])],
        [sg.Text("Oficina:")],
        [sg.InputCombo(("Vertical","Horizontal"), size=(10, 1),default_value=data["oficina"])],
        [sg.Submit("Guardar cambios"),sg.Cancel("Volver")],
        ]

 window=sg.Window("Configuracion",size=(700,700), font='Courier').Layout(layout)

 while True:
  button, values = window.Read()
  Lista=data["palabras"]
  if button=="Guardar cambios":
     datosConfig={}
     datosConfig["palabras"]=sorted(Lista, key=lambda palabra: len(palabra), reverse=True)
     datosConfig["colores"]={"Sustantivos":values[0],"Verbos":values[1],"Adjetivos":values[2]}
     datosConfig["orientacion"]=values[3]
     datosConfig["cantidad"]={"Sustantivos":values[4],"Verbos":values[5],"Adjetivos":values[6]}
     datosConfig["mayus"]=values[7]
     datosConfig["titulos"]=values[8]
     datosConfig["textos"]=values[9]
     datosConfig["estilo"]=values[10]
     datosConfig["oficina"]=values[11]
     with open("configuracion.json", "w") as j:
        json.dump(datosConfig,j)

  if button=="Volver"or values==None:
     exit(19)
  if button=="Agregar":
      Lista.append(values['input'])      
      window.FindElement('list').Update(values=(Lista))
      window.FindElement('input').Update('')   
  if button=="Quitar":
      try:
       Lista.remove(values['input'])
      except(ValueError):
          sg.PopupError("No se puede quitar la palabra por que no existe en la lista")        
      window.FindElement('list').Update(values=(Lista))
    
 window.Close()

##########################################################################################
#Main
sg.ChangeLookAndFeel('BrownBlue')

layout=[    
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

window = sg.Window("Juego Educativo",size=(290,375), font='Courier').Layout(layout)

while True:
 button, values = window.Read()
 if button=="Jugar":
    jugar()
 if button=="Configuracion":
    configuracion()
 if button=="Salir"or values==None:
     exit(19)
    
window.Close()
