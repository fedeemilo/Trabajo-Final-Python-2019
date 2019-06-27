import PySimpleGUI as sg
import json
import random
import clasificar as c

#CONFIGURACIÓN DEL JUEGO
def configuracion():
 with open('configuracion.json', encoding='utf-8') as f:
     data = json.load(f)

 #diccionario de colores donde la clave es el nombre del color en español que será mostrado en 
 #la interfaz gráfica y el valor está en ingles para poder modificar el atributo de cambio de color 
 #del sg.Text
 color={
        "rojo": "red",
        "azul": "blue",
        "verde": "green",
        "naranja": "orange",
        "amarillo": "yellow",
        "gris": "gray",
        "violeta": "purple",
        "rosa": "pink",
        "marron": "brown"
       }

 #Lista con varios nombres de tipografías para configurar los títulos y los textos que se usaran en el reporte
 tipografias = [
                'Arial', 'Arial Black',  'Helvetica', 'Impact', 'Lucida Sans Unicode', 'Tahoma',
                'Courier', 'Verdana', 'Lucida Console'
               ]
 
 #Estilos Look and Feel -> este estilo se elegirá en base al promedio de temperaturas
 #registrado en todas las oficinas (debemos asignarle un color a cierto rango de temperaturas!!)
 estilos = ['NeutralBlue', 'Purple', 'GreenTan', 'BluePurple', 'BrightColors']

 #Lista con las diferentes oficinas en las que se analizará la temperatura
 oficinas = ['oficina1', 'oficina2', 'oficina3', 'oficina4', 'oficina5']

 colum_estilo =  [
                  [sg.Text("Estilo", relief='raised', text_color='black')],
                  [sg.InputCombo(estilos,
                    size=(9, 1),
                    default_value=data["estilo"], 
                    key='estilos', 
                    readonly=True)]
                 ]

 colum_oficina = [
                  [sg.Text("Oficina", relief='raised', text_color='black')],
                  [sg.InputCombo(oficinas,
                    size=(9, 1),
                    default_value=data["oficina"], 
                    key='oficinas', 
                    readonly=True)]
                 ]

 colum_titulos = [
                  [sg.Text("Títulos", relief='groove'),
                   sg.InputCombo(tipografias,   
                    size=(9, 1),
                    default_value=data["titulos"], 
                    key='titulos', 
                    readonly=True)]
                 ]

 colum_textos = [
                  [sg.Text("Textos", relief='groove'),
                   sg.InputCombo(tipografias, 
                    size=(9, 1),
                    default_value=data["textos"], 
                    key='textos', 
                    readonly=True)],
                ]

 layout=[
          [sg.Text(" Configurar palabras ", relief='raised', text_color='black')],
          [sg.Text("Ingrese una palabra", size=(20,1), relief='groove'), sg.InputText(key='input', size=(20,3))],
          [sg.Listbox(values=(data["palabras"]),key="list", size=(50,3))],
          [sg.Submit("Agregar"),sg.Submit("Quitar")],
          [sg.Text("Colores", relief='raised', text_color='black')],
          [sg.T('Sust'), sg.InputCombo((list(color.keys())), 
              size=(9, 1), 
              key='color_sust', 
              default_value='rojo', 
              readonly=True), 
            sg.T('Verbs'), sg.InputCombo((list(color.keys())), 
              size=(9, 1), 
              key='color_verb', 
              default_value='verde', 
              readonly=True), 
            sg.T('Adj'), sg.InputCombo((list(color.keys())), 
              size=(9, 1), 
              key='color_adj', 
              default_value='azul', 
              readonly=True)],
          [sg.Text("Orientacion", relief='raised', text_color='black')],
          [sg.InputCombo(("Vertical","Horizontal"), 
            size=(10, 1),
            default_value=data["orientacion"], 
            key='vert_horiz', 
            readonly=True)],
          [sg.Text("Cantidad de palabras", relief='raised', text_color='black')],
          [sg.Text("Sustantivos:", size=(12,1),),sg.InputText(
                                                  size=(3,1),
                                                  default_text =data["cantidad"]["Sustantivos"], 
                                                  key='cant_sust'),
            sg.Text("Verbos:", size=(7,1)),sg.InputText(
                                                  size=(3,1),
                                                  default_text =data["cantidad"]["Verbos"], 
                                                  key='cant_verb'),
            sg.Text("Adjetivos:", size=(10,1)),sg.InputText(
                                                size=(3,1),
                                                default_text =data["cantidad"]["Verbos"], 
                                                key='cant_adj')],
          [sg.Text("Mayúsculas/Minúsculas", relief='raised', text_color='black')],
          [sg.InputCombo(("Mayúsculas","Minúsculas"), 
            size=(10, 1),
            default_value=data["mayus"], 
            key='mayus', 
            readonly=True)],
          [sg.Text("Tipografías de títulos y texto para el reporte", relief='raised', text_color='black')],
          [sg.Column(colum_titulos), sg.Column(colum_textos)],
          [sg.Text("Datos que provienen de los sensores de Raspberry Pi", relief='raised', text_color='black')],
          [sg.Column(colum_estilo), sg.Column(colum_oficina)],
          [sg.T('Opciones de ayuda para el alumno', relief='raised', font='Courier')],
          [sg.Checkbox('Lista de palabras', key='check_lista'), 
           sg.Checkbox('Definiciones de las palabras', key='check_def')],
          [sg.Submit("Guardar cambios"),sg.Cancel("Volver")],
        ]

 window_config = sg.Window("Configuración",
                  size=(570,670), 
                  font='Courier', 
                  no_titlebar=True,
                  grab_anywhere=True).Layout(layout)

 lista_adjetivos = []
 lista_sustantivos = []
 lista_verbos = []

 while True:
  button, values = window_config.Read()
  Lista = data["palabras"]

  cant_sust = int(data["cantidad"]["Sustantivos"])
  cant_verb = int(data["cantidad"]["Verbos"])
  cant_adj = int(data["cantidad"]["Adjetivos"])

  if button == "Guardar cambios":
  
     #ÉSTO GENERA UN PROBLEMA!!
     Lista =[]
     if len(lista_sustantivos) >= cant_sust:
      Lista.extend(random.sample(lista_sustantivos, k=cant_sust))
     else:
      Lista.extend(lista_sustantivos)
     if len(lista_verbos) >= cant_verb:
      Lista.extend(random.sample(lista_verbos, k=cant_verb))
     else:
      Lista.extend(lista_verbos)
     if len(lista_adjetivos)>= cant_adj:
      Lista.extend(random.sample(lista_adjetivos, k=cant_adj))
     else:
      Lista.extend(lista_adjetivos) 



     #Se cargan los datos de la configuracion para cargarlos en configuracion.json
     datosConfig = {}
     datosConfig["palabras"] = sorted(Lista, key=lambda palabra: len(palabra), reverse=True)
     datosConfig["colores"] = {
                                "Sustantivos": color[values['color_sust']],
                                "Verbos": color[values['color_verb']],
                                "Adjetivos": color[values['color_adj']]
                              }
     datosConfig["orientacion"]= values['vert_horiz']
     datosConfig["cantidad"] = {
                                "Sustantivos":  values['cant_sust'],
                                "Verbos": values['cant_verb'],
                                "Adjetivos": values['cant_adj']
                               }
     datosConfig["mayus"] = values['mayus']
     datosConfig["titulos"] = values['titulos']
     datosConfig["textos"] = values['textos']
     datosConfig["estilo"] = values['estilos'] 
     datosConfig["oficina"] = values['oficinas'] 
     datosConfig["sustantivos"] = lista_sustantivos
     datosConfig["verbos"] = lista_verbos
     datosConfig["adjetivos"] = lista_adjetivos

     if values['check_lista'] & values['check_def']:
      datosConfig['ayuda'] = ['si', 'si']
     elif values['check_lista'] &  values['check_def']:
      datosConfig['ayuda'] = ['si', 'no']
     elif values['check_lista'] & values['check_def']:
      datosConfig['ayuda'] = ['no', 'si']
     else:
      datosConfig['ayuda'] = ['no', 'no']

     with open("configuracion.json", "w+", encoding='utf-8') as j:
        json.dump(datosConfig , j, indent=4, ensure_ascii=False)

     sg.Popup('La configuración ha sido guardada con éxito.', font='Courier')
     break

  if button=="Volver" or values==None:
     break

  if button=="Agregar":
    try:
      #Pattern -> a medida que se van agregando palabras se consulta a pattern si existe, sino
      #a Wiktionary enviando su correspondiente reporte en caso de que no exista 
      input_palabra = values['input']
      
      #clasifico la palabra ingresada utilizando módulos de pattern.es
      #si la función retorna false entonces no se ha encontrado y procedo a buscarla en wiktionary
      palabra_clasificada = c.clasificar(input_palabra)[0]
      print(palabra_clasificada)
      
      if palabra_clasificada == False:
        #busco la palabra en wiktionary
        print('buscando en wiktionary')
      else:
        if palabra_clasificada[1] == 'NN':
          lista_sustantivos.append(palabra_clasificada[0])
        elif palabra_clasificada[1] == 'VB':
          lista_verbos.append(palabra_clasificada[0])
        elif palabra_clasificada[1] == 'JJ':
          lista_adjetivos.append(palabra_clasificada[0])   
             

      Lista.append(palabra_clasificada[0])      
      window_config.FindElement('list').Update(values=(Lista))
      window_config.FindElement('input').Update('') 
    except TypeError:
      sg.Popup('Debes ingresar una palabra', 
        font='Courier', 
        no_titlebar=True, 
        background_color='red',
        grab_anywhere=True)
  if button=="Quitar":
      try:
       Lista.remove(values['list'][0])
      except(ValueError):
          sg.PopupError("No se puede quitar la palabra por que no existe en la lista")        
      window_config.FindElement('list').Update(values=(Lista))
    
 window_config.Close()
