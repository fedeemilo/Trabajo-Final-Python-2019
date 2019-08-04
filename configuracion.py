import PySimpleGUI as sg
import json
import random

from clasificar import clasificar_wikt, clasificar_pattern


def guardarCambios():
     
       if len(data['palabras']) != 0:
        Lista = data['palabras'].copy()
       else:
        Lista =[]

        #________________________________________________________
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
        #_________________________________________________________

       #Me aseguro de que la lista no tenga palabras que se repitan
       Lista = list(set(Lista))


       #Se cargan los datos de la configuracion para cargarlos en configuracion.json
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

       #levanto una excepción en el caso de que los input para la cantidad de 
       #tipos de palabras esten todos seteados en 0(cero)
       if datosConfig['cantidad']['Sustantivos'] == '0' and datosConfig['cantidad']['Adjetivos'] == '0' and datosConfig['cantidad']['Verbos'] == '0':
        raise ValueError

       #CONFIGURACIÓN DE AYUDA PARA EL ALUMNO
       #_______________________________________________
       #lista y definiciones activadas
       if values['check_lista'] & values['check_def']:
        datosConfig['ayuda'] = ['si', 'si']
       #lista activada 
       elif values['check_lista']:
        datosConfig['ayuda'] = ['si', 'no']
       #definiciones activadas 
       elif values['check_def']:
        datosConfig['ayuda'] = ['no', 'si']
       #ayuda desactivada
       else:
        datosConfig['ayuda'] = ['no', 'no']
       #_______________________________________________

       with open("configuracion.json", "w+", encoding='utf-8') as j:
          json.dump(datosConfig , j, indent=4, ensure_ascii=False)

       sg.Popup('La configuración ha sido guardada con éxito.', 
        font='Courier', 
        background_color='green',
        no_titlebar=True,
        button_color=('white', 'green'),
        grab_anywhere=True)
     

















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
                  [sg.Text("Estilo", 
                    relief='groove', 
                    text_color='white',
                    background_color='dark slate gray'),
                  sg.InputCombo(estilos,
                    size=(14, 1),
                    default_value=data["estilo"], 
                    key='estilos', 
                    readonly=True,
                    background_color='dark slate gray')]
                 ]

 colum_oficina = [
                  [sg.Text("Oficina", 
                    relief='groove', 
                    text_color='white',
                    background_color='dark slate gray'),
                  sg.InputCombo(oficinas,
                    size=(14, 1),
                    default_value=data["oficina"], 
                    key='oficinas', 
                    readonly=True,
                    background_color='dark slate gray')]
                 ]

 colum_titulos = [
                  [sg.Text("Títulos", 
                    relief='groove', 
                    background_color='dark slate gray',
                    text_color='white'),
                   sg.InputCombo(tipografias,   
                    size=(14, 1),
                    default_value=data["titulos"], 
                    key='titulos', 
                    readonly=True,
                    background_color='dark slate gray')]
                 ]

 colum_textos = [
                  [sg.Text("Textos", 
                    relief='groove', 
                    background_color='dark slate gray',
                    text_color='white'),
                   sg.InputCombo(tipografias, 
                    size=(14, 1),
                    default_value=data["textos"], 
                    key='textos', 
                    readonly=True,
                    background_color='dark slate gray')],
                ]

 layout=[
          [sg.Text("  Configuración del juego ", 
            relief='raised', 
            text_color='white',
            background_color='dark slate gray',
            size=(26,1),
            font=('Courier', 14, 'bold'))],
          [sg.Text("Ingrese una palabra", 
            text_color='white',
            size=(20,1), 
            relief='groove',
            background_color = '#2F2F4F'), sg.InputText(
                              key='input', 
                              size=(20,3))],
          [sg.Listbox(values=(data["palabras"]),key="list", size=(50,3))],
          [sg.Submit("Agregar"),sg.Submit("Quitar", button_color=('white','red'))],
          [sg.Text("Colores", 
            relief='raised', 
            text_color='white',
            background_color='dark slate gray', 
            font=('Courier', 13, 'bold'))],
          [sg.T('Sust', background_color='dark slate gray', text_color='white'), sg.InputCombo((list(color.keys())), 
              size=(9, 1), 
              key='color_sust', 
              default_value='rojo', 
              readonly=True), 
            sg.T('Verbs', background_color='dark slate gray', text_color='white'), sg.InputCombo((list(color.keys())), 
              size=(9, 1), 
              key='color_verb', 
              default_value='verde', 
              readonly=True), 
            sg.T('Adj', background_color='dark slate gray', text_color='white'), sg.InputCombo((list(color.keys())), 
              size=(9, 1), 
              key='color_adj', 
              default_value='azul', 
              readonly=True)],
          [sg.Text("Orientación", 
            relief='raised', 
            background_color='dark slate gray',
            text_color='white', 
            font=('Courier', 13, 'bold'))],
          [sg.InputCombo(("Vertical","Horizontal"), 
            size=(10, 1),
            default_value=data["orientacion"], 
            key='vert_horiz', 
            readonly=True)],
          [sg.Text("Cantidad de palabras", 
            relief='raised',
            background_color='dark slate gray', 
            text_color='white', 
            font=('Courier', 13, 'bold'))],
          [sg.Text("Sustantivos:", size=(12,1), background_color='dark slate gray', text_color='white'),sg.InputText(
                                                  size=(3,1),
                                                  default_text =data["cantidad"]["Sustantivos"], 
                                                  key='cant_sust'),
            sg.Text("Verbos:", size=(7,1), background_color='dark slate gray', text_color='white'),sg.InputText(
                                                  size=(3,1),
                                                  default_text =data["cantidad"]["Verbos"], 
                                                  key='cant_verb'),
            sg.Text("Adjetivos:", size=(10,1), background_color='dark slate gray', text_color='white'),sg.InputText(
                                                size=(3,1),
                                                default_text =data["cantidad"]["Verbos"], 
                                                key='cant_adj')],
          [sg.Text("Mayúsculas/Minúsculas", 
            relief='raised', 
            text_color='white',
            background_color='dark slate gray', 
            font=('Courier', 13, 'bold'))],
          [sg.InputCombo(("Mayúsculas","Minúsculas"), 
            size=(10, 1),
            default_value=data["mayus"], 
            key='mayus', 
            readonly=True)],
          [sg.Text("Tipografías de títulos y texto para el reporte", 
            relief='raised', 
            text_color='white',
            background_color='dark slate gray',
            font=('Courier', 13, 'bold'))],
          [sg.Column(colum_titulos, 
            background_color = 'dark slate gray'), 
          sg.Column(colum_textos, 
            background_color = 'dark slate gray')],
          [sg.Text("Datos que provienen de los sensores de Raspberry Pi", 
            relief='raised', 
            background_color='dark slate gray',
            text_color='white',
            font=('Courier', 13, 'bold'))],
          [sg.Column(colum_estilo, 
            background_color = 'dark slate gray'), 
          sg.Column(colum_oficina, 
            background_color = 'dark slate gray')],
          [sg.T('Opciones de ayuda para el alumno', 
            relief='raised',  
            text_color='white',
            background_color='dark slate gray',
            font=('Courier', 13, 'bold'))],
          [sg.Checkbox('Lista de palabras', 
            key='check_lista',
            text_color='white',
            background_color='dark slate gray'), 
           sg.Checkbox('Definiciones/Palabras clave', 
            key='check_def',
            text_color='white',
            background_color='dark slate gray')],
          [sg.Submit("Guardar cambios"), 
           sg.Button('Limpiar Json', 
            key='limpiar',
            font='Courier'),
           sg.Button("Volver a Inicio", 
            key='volver', 
            font=('Courier', 12, 'bold'))]
        ]

 window_config = sg.Window("Configuración",
                  size=(570,663), 
                  font='Courier', 
                  no_titlebar=True,
                  grab_anywhere=True,
                  background_color='dark slate gray').Layout(layout)

 
 datosConfig = {}
 lista_adjetivos = []
 lista_sustantivos = []
 lista_verbos = []

 if len(data['sustantivos']) > 0:
  lista_sustantivos.extend(data['sustantivos'])
 if len(data['adjetivos']) > 0:
  lista_adjetivos.extend(data['adjetivos'])
 if len(data['verbos']) > 0:
  lista_verbos.extend(data['verbos'])

 while True:
  button, values = window_config.Read()
  Lista = data["palabras"]

  cant_sust = int(data["cantidad"]["Sustantivos"])
  cant_verb = int(data["cantidad"]["Verbos"])
  cant_adj = int(data["cantidad"]["Adjetivos"])

  if button == "Guardar cambios":
    try:
     guardarCambios()
     break
    except ValueError:
      sg.Popup('Los input para la cantidad de tipos de palabras no pueden estar todos en 0(cero)',
      background_color='orange',
      button_color=('white', 'orange'),
      font=('Courier', 13, 'bold'),
      no_titlebar=True) 

  if button == "volver" or values == None:
     break

  elif button=="Agregar":
    input_palabra = values['input']
    #A medida que voy agregando las palabras primero se consulta en Wiktionary si la
    #misma existe. En caso afirmativo se la clasifica (adj, sust o verb). También se 
    #deberá verificar que la info obtenida coincida con lo reportado por pattern.es. 
    #Si la clasificación de la palabra no coincide entonces ésto deberá ser informado
    #en un reporte, tomando la clasificación de Wiktionary como válida. Si la palabra
    #no se encuentra en wiktionary pero sí en pattern.es, se tomará la clasificación
    #de pattern y se le pedirá al docente que ingrese una defininción, marcando que
    #se utilizará una definición guardada en un archivo local y no en Wiktionary. 
    #Si la palabra no se encuentra en ningún recurso entonces no se incluirá y 
    #también se incluirá ésto en un reporte.
    encontro_wik = False
    encontro_patt = False
    palabra_clasificada = clasificar_wikt(input_palabra)
    if palabra_clasificada != False:
      #La encontró en Wiktionary
      encontro_wik = True
      if palabra_clasificada[2] == 'NN':
        lista_sustantivos.append(palabra_clasificada[0])
      elif palabra_clasificada[2] == 'VB' or palabra_clasificada[1] == 'VBN':
         lista_verbos.append(palabra_clasificada[0])
      elif palabra_clasificada[2] == 'JJ':
         lista_adjetivos.append(palabra_clasificada[0])
    else:
      #No la encontró en wiktionary, así que la busco en pattern

      palabra_clasificada = clasificar_pattern(input_palabra)
      if palabra_clasificada != False:
        #Primero debo solicitar al docente que ingrese una definición para la palabra
        definicion_docente = sg.PopupGetText('Ingrese una definición para la palabra encontrada en pattern.es',
        background_color='dark slate gray',
        button_color=('white', 'dark slate gray'),
        no_titlebar=True,
        font=('Courier', 13, 'bold'),
          text_color='white')
        #La encontró en pattern
        print('No la encontró en Wiktionary pero sí en Pattern')
        
        encontro_patt = True
        if palabra_clasificada[0][1] == 'NN':
          lista_sustantivos.append(palabra_clasificada[0])
        elif palabra_clasificada[0][1] == 'VB' or palabra_clasificada[1] == 'VBN':
          lista_verbos.append(palabra_clasificada[0])
        elif palabra_clasificada[0][1] == 'JJ':
          lista_adjetivos.append(palabra_clasificada[0])
      else:
        #No la encontró en pattern ni en wiktionary 
        sg.Popup('La palabra no se encuentra en ninguno de los recursos utilizados. Se añadirá ésta situación en un reporte.', 
              background_color='red',
              button_color=('white','red'),
              no_titlebar=True,
              font=('Courier', 13, 'bold'))
        continue
    if encontro_wik:
      Lista.append(palabra_clasificada[0])   
    elif encontro_patt:
      Lista.append(palabra_clasificada[0][0])   
    window_config.FindElement('list').Update(values=(Lista))
    window_config.FindElement('input').Update('') 
  elif button=="Quitar":
      try:
  
       palabra_a_borrar = values['list'][0]
       Lista.pop(data['palabras'].index(palabra_a_borrar))
       
      except ValueError:
          sg.PopupError("No se puede quitar la palabra por que no existe en la lista")  
      except IndexError:
          sg.Popup('No hay ninguna palabra para quitar', 
            font='Courier',
            background_color='red',
            button_color=('white', 'red'),
            no_titlebar=True)
      window_config.FindElement('list').Update(values=(Lista))
  elif button == 'limpiar':
    with open('configuracion.json', 'w+', encoding='utf-8') as f:
      datosConfig["palabras"] = []
      datosConfig["colores"] = {
                                "Sustantivos": 'red',
                                "Verbos": 'green',
                                "Adjetivos": 'blue'
                              }
      datosConfig["orientacion"] = 'Horizontal'
      datosConfig["cantidad"] = {
                                "Sustantivos":  '0',
                                "Verbos": '0',
                                "Adjetivos": '0'
                               }
      datosConfig["mayus"] = 'Minúsculas'
      datosConfig["titulos"] = 'Arial'
      datosConfig["textos"] = 'Arial'
      datosConfig["estilo"] = 'GreenTan'
      datosConfig["oficina"] = 'oficina1'
      datosConfig["sustantivos"] = []
      datosConfig["verbos"] = []
      datosConfig["adjetivos"] = []
      datosConfig['ayuda'] = ['no', 'no']

      json.dump(datosConfig, f, indent=4, ensure_ascii=False)
      sg.Popup('El archivo configuracion.json ha sido limpiado con éxito!', 
        background_color='green',
        button_color=('white', 'green'),
        font=('Courier', 13, 'bold'),
        no_titlebar=True)
      break
    
 window_config.Close()
 #---------------------------------------------------------------------------------------------