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
                    background_color='dark slate gray'),
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
                    background_color='dark slate gray'),
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
            text_color='black',
            background_color='dark slate gray',
            size=(26,1),
            font=('Courier', 14, 'bold'))],
          [sg.Text("Ingrese una palabra", 
            size=(20,1), 
            relief='groove',
            background_color = '#2F2F4F'), sg.InputText(
                              key='input', 
                              size=(20,3))],
          [sg.Listbox(values=(data["palabras"]),key="list", size=(50,3))],
          [sg.Submit("Agregar"),sg.Submit("Quitar", button_color=('white','red'))],
          [sg.Text("Colores", 
            relief='raised', 
            text_color='black', 
            font=('Courier', 12, 'bold'))],
          [sg.T('Sust', background_color='dark slate gray'), sg.InputCombo((list(color.keys())), 
              size=(9, 1), 
              key='color_sust', 
              default_value='rojo', 
              readonly=True), 
            sg.T('Verbs', background_color='dark slate gray'), sg.InputCombo((list(color.keys())), 
              size=(9, 1), 
              key='color_verb', 
              default_value='verde', 
              readonly=True), 
            sg.T('Adj', background_color='dark slate gray'), sg.InputCombo((list(color.keys())), 
              size=(9, 1), 
              key='color_adj', 
              default_value='azul', 
              readonly=True)],
          [sg.Text("Orientación", 
            relief='raised', 
            text_color='black', 
            font=('Courier', 12, 'bold'))],
          [sg.InputCombo(("Vertical","Horizontal"), 
            size=(10, 1),
            default_value=data["orientacion"], 
            key='vert_horiz', 
            readonly=True)],
          [sg.Text("Cantidad de palabras", 
            relief='raised', 
            text_color='black', 
            font=('Courier', 12, 'bold'))],
          [sg.Text("Sustantivos:", size=(12,1), background_color='dark slate gray'),sg.InputText(
                                                  size=(3,1),
                                                  default_text =data["cantidad"]["Sustantivos"], 
                                                  key='cant_sust'),
            sg.Text("Verbos:", size=(7,1), background_color='dark slate gray'),sg.InputText(
                                                  size=(3,1),
                                                  default_text =data["cantidad"]["Verbos"], 
                                                  key='cant_verb'),
            sg.Text("Adjetivos:", size=(10,1), background_color='dark slate gray'),sg.InputText(
                                                size=(3,1),
                                                default_text =data["cantidad"]["Verbos"], 
                                                key='cant_adj')],
          [sg.Text("Mayúsculas/Minúsculas", 
            relief='raised', 
            text_color='black', 
            font=('Courier', 12, 'bold'))],
          [sg.InputCombo(("Mayúsculas","Minúsculas"), 
            size=(10, 1),
            default_value=data["mayus"], 
            key='mayus', 
            readonly=True)],
          [sg.Text("Tipografías de títulos y texto para el reporte", 
            relief='raised', 
            text_color='black',
            font=('Courier', 12, 'bold'))],
          [sg.Column(colum_titulos, 
            background_color = 'dark slate gray'), 
          sg.Column(colum_textos, 
            background_color = 'dark slate gray')],
          [sg.Text("Datos que provienen de los sensores de Raspberry Pi", 
            relief='raised', 
            text_color='black',
            font=('Courier', 12, 'bold'))],
          [sg.Column(colum_estilo, 
            background_color = 'dark slate gray'), 
          sg.Column(colum_oficina, 
            background_color = 'dark slate gray')],
          [sg.T('Opciones de ayuda para el alumno', 
            relief='raised',  
            text_color='black',
            font=('Courier', 12, 'bold'))],
          [sg.Checkbox('Lista de palabras', 
            key='check_lista',
            background_color='dark slate gray'), 
           sg.Checkbox('Definiciones de las palabras', 
            key='check_def',
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
     break

  if button == "volver" or values == None:
     break

  elif button=="Agregar":
    input_palabra = values['input']
    if input_palabra in values['list']:
      sg.Popup('Ésta palabra ya se encuentra en la lista, elige otra porfavor.', 
        background_color='orange',
        button_color=('white','orange'),
        font=('Courier', 13, 'bold'),
        no_titlebar=True)
    else:
      try:
        #Pattern -> a medida que se van agregando palabras se consulta a pattern si existe, sino
        #a Wiktionary enviando su correspondiente reporte en caso de que no exista 
        
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
          elif palabra_clasificada[1] == 'VB' or palabra_clasificada[1] == 'VBN':
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
          grab_anywhere=True,
          button_color=('white', 'red'))
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