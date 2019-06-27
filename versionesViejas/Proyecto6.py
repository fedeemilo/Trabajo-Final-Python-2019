import PySimpleGUI as sg
import string 
import random
import json
import pattern.es
from pattern.web import Wiktionary,plaintext
#--------------------------------------------------------------------------------------------------------------------
#Funciones

def sopa():
    retorno=[]
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
      palabras[word]["coord"]=[]
      num=random.randint(0,(n-len(word)))
      for i in range(num):
       layout[f].append(sg.T(random.choice(string.ascii_lowercase), size=(7,2), background_color='green', pad=(0.5,0.5), justification='center', key=i , click_submits=True, enable_events=True))
      for i in range(len(word)):
       layout[f].append(sg.T(word[i], size=(7,2), background_color='green', pad=(0.5,0.5), justification='center', key=(f,num+i) , click_submits=True, enable_events=True))
       palabras[word]["coord"].append((f,num+i))
      for i in range(n-len(word)-num):
       layout[f].append(sg.T(random.choice(string.ascii_lowercase), size=(7,2), background_color='green', pad=(0.5,0.5), justification='center', key=i , click_submits=True, enable_events=True))
     retorno.append(layout)
     retorno.append(palabras)
     return retorno
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
      palabras[word]["coord"]=[]
      num=random.randint(0,(m-len(word)))
      for c in range(num):
        layout[c].append(sg.T(random.choice(string.ascii_lowercase), size=(7,2), background_color='green', pad=(0.5,0.5), justification='center', key=i , click_submits=True, enable_events=True))
      for c in range(len(word)):
        layout[c+num].append(sg.T(word[c], size=(7,2), background_color='green', pad=(0.5,0.5), justification='center', key=(c+num,f) , click_submits=True, enable_events=True))
        palabras[word]["coord"].append((c+num,f))
      for c in range(num+len(word),m):
        layout[c].append(sg.T(random.choice(string.ascii_lowercase), size=(7,2), background_color='green', pad=(0.5,0.5), justification='center', key=i , click_submits=True, enable_events=True)) 
     retorno.append(layout)
     retorno.append(palabras) 
     return layout,palabras  
def jugar():
    with open('configuracion.json') as f:
     data = json.load(f)
    retorno=sopa()
    layout=retorno[0]
    palabras=retorno[1]
    window = sg.Window('Sopa de letras',size=(1280,720), grab_anywhere=True, font='Courier').Layout(layout)
    while True:
      event, values = window.Read()
      if values==None:
       break
      continuar=True
      sacar=False
      for i in palabras.keys():
        if event==palabras[i]["coord"][0]:
         window.FindElement(event).Update(background_color='red')
         x=1
         while (continuar) and (x<len(i)):
           event, values = window.Read() 
           if palabras[i]["coord"][x]==event:
            window.FindElement(event).Update(background_color='red')
            x=x+1
           else:
            continuar=False
         if continuar==False:   
           for j in range(x):
            window.FindElement(palabras[i]["coord"][j]).Update(background_color='green') 
         else:
          sacar=True
          quitar=i
      if sacar:
        palabras.pop(quitar)
      if len(palabras)==0:
         sg.PopupError("Ganaste") 
         exit(19)
def configuracion():
 with open('configuracion.json') as f:
     data = json.load(f)
 color=["red","blue","green","orange","yellow","gray","purple","pink","brown"]
 layout=[
          [sg.Text(" Configurar palabras ", relief='raised', text_color='black')],
          [sg.Text("Ingrese una palabra", size=(20,1), relief='groove'), sg.InputText(key='input', size=(20,3))],
          [sg.Listbox(values=(data["palabras"]),key="list", size=(50,3))],
          [sg.Submit("Agregar"),sg.Submit("Quitar")],
          [sg.Text("Colores", relief='raised', text_color='black')],
          [sg.ColorChooserButton('Sustantivos', size=(11, 1), key='color_sust', button_color=('white', 'red')), 
            sg.ColorChooserButton('Verbos', size=(10, 1), key='color_verb', button_color=('white', 'green')), 
            sg.ColorChooserButton('Adjetivos', size=(10, 1), key='color_adj', button_color=('white', 'blue'))],
          [sg.Text("Orientacion", relief='raised', text_color='black')],
          [sg.InputCombo(("Vertical","Horizontal"), size=(10, 1),default_value=data["orientacion"], key='vert_horiz')],
          [sg.Text("Cantidad de palabras", relief='raised', text_color='black')],
          [sg.Text("Sustantivos:", size=(12,1),),sg.InputText(size=(3,1),default_text =data["cantidad"]["Sustantivos"], key='cant_sust'),
            sg.Text("Verbos:", size=(7,1)),sg.InputText(size=(3,1),default_text =data["cantidad"]["Verbos"], key='cant_verb'),
            sg.Text("Adjetivos:", size=(10,1)),sg.InputText(size=(3,1),default_text =data["cantidad"]["Verbos"], key='cant_adj')],
          [sg.Text("Mayúsculas/Minúsculas", relief='raised', text_color='black')],
          [sg.InputCombo(("Mayúsculas","Minúsculas"), size=(10, 1),default_value=data["mayus"], key='mayus')],
          [sg.Text("Tipografías de títulos y texto para el reporte", relief='raised', text_color='black')],
          [sg.Text("Tútulos", relief='groove'),sg.InputCombo((color), size=(5, 1),default_value=data["titulos"], key='titulos')],
          [sg.Text("Textos", relief='groove'),sg.InputCombo((color), size=(5, 1),default_value=data["textos"], key='textos')],
          [sg.Text("Estilo", relief='raised', text_color='black')],
          [sg.InputCombo(("Vertical","Horizontal"), size=(10, 1),default_value=data["estilo"], key='estilo')],
          [sg.Text("Oficina", relief='raised', text_color='black')],
          [sg.InputCombo(("Vertical","Horizontal"), size=(10, 1),default_value=data["oficina"], key='oficina')],
          [sg.Submit("Guardar cambios"),sg.Cancel("Volver")],
        ]

 window=sg.Window("Configuración",size=(570,670), font='Courier').Layout(layout)

 while True:
  button, values = window.Read()
  Lista=data["palabras"]

  if button=="Guardar cambios":
     datosConfig={}
     datosConfig["palabras"]=sorted(Lista, key=lambda palabra: len(palabra), reverse=True)
     datosConfig["colores"]={"Sustantivos":values['color_sust'],"Verbos":values['color_verb'],"Adjetivos":values['color_adj']}
     datosConfig["orientacion"]=values['vert_horiz']
     datosConfig["cantidad"]={"Sustantivos":values['cant_sust'],"Verbos":values['cant_verb'],"Adjetivos":values['cant_adj']}
     datosConfig["mayus"]=values['mayus']
     datosConfig["titulos"]=values['titulos']
     datosConfig["textos"]=values['textos']
     datosConfig["estilo"]=values['estilo']
     datosConfig["oficina"]=values['oficina']
     with open("configuracion.json", "w") as j:
        json.dump(datosConfig,j)

  if button=="Volver"or values==None:
     break
  if button=="Agregar":
      Lista.append(values['input'])      
      window.FindElement('list').Update(values=(Lista))
      window.FindElement('input').Update('') 
      print(values['list'])
  if button=="Quitar":
      try:
       Lista.remove(values['list'][0])
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
