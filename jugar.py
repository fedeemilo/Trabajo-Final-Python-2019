import PySimpleGUI as sg
import json
from sopa import sopa
def jugar():
    """La funcion carga la configuracion.json para permitir al usuario jugar a la sopa de letras."""
    #Archivo Json

    try:
      with open('configuracion.json', encoding='utf-8') as f:
       data = json.load(f)
      #Se llama a la funcion sopa() para cargar el layout que contiene a la sopa, un diccionario de palabras con su color dependiente su tipo(sust,adj o verb) y las coordenadas de cada letra
      #y una lista con las coordenadas de los espacios con letras randoms
      retorno = sopa()
      layout = retorno[0]
      palabras = retorno[1]
      letras = retorno[2]

      longitud_lista_pal = len(list(palabras.keys()))
     
      #variables con el ancho y la altura de la caja que contiene cada letra
      ancho = 8
      altura = 2

      ayuda = [
                [sg.T('*Encuentra las ' + str(longitud_lista_pal) + ' palabras*')],
                [sg.T('', background_color='dark slate gray')],
                [sg.Button('Pedir Ayuda!', key='help')],
                [sg.Listbox(values=[], font='Courier', size=(10,7), key='lista_pal',enable_events=True, visible=data['ayuda'][0] == 'si')]
              ]

      tipos_de_palabras = [
                            [sg.T('', background_color='dark slate gray')],
                            [sg.Text(" Sustantivos  ",
                              text_color='white', 
                              font=('Courier', 12, 'bold'),
                              background_color='dark slate gray'),
                              sg.T(
                                "",
                                size=(2,1),
                                background_color=str(data["colores"]["Sustantivos"])),
                              sg.Radio('', "RADIO1",
                                key="rad_sust",
                                size=(10,1),
                                text_color="white",
                                default=True,
                                background_color='dark slate gray')],
                             [sg.Text(" Verbos       ",
                              text_color='white', 
                              font=('Courier', 12, 'bold'),
                              background_color='dark slate gray'),
                              sg.T(
                                "",
                                size=(2,1),
                                background_color=data["colores"]["Verbos"],
                                ),
                              sg.Radio('', "RADIO1",
                                key="rad_verb",
                                size=(10,1),
                                text_color="white",
                                background_color='dark slate gray'),
                             ],
                             [sg.Text(' Adjetivos    ',
                              text_color='white', 
                              font=('Courier', 12, 'bold'),
                              background_color='dark slate gray'),
                              sg.T(
                                "",
                                size=(2,1),
                                background_color=data["colores"]["Adjetivos"],
                                ),
                              sg.Radio('', "RADIO1",
                                key="rad_adj",
                                size=(10,1),
                                text_color="white",
                                background_color='dark slate gray')],
                              [sg.T('', background_color='dark slate gray')],
                              [sg.Submit("¿Completé correctamente todo?", key='revisar')], 
                              [sg.Button('Volver a Inicio', key='volver', font=('Courier', 12, 'bold'))]
                          ]

      #tabla contiene  datos que ayudaran al usuario como:cantidad de sustantivos,adjetivos y verbos. 
      #Ademas el color seleccionado para pintar cada letra en la sopa
      tabla=[ 
                [sg.Column(tipos_de_palabras, 
                  background_color='dark slate gray'), 
                sg.Column(ayuda,
                  background_color='dark slate gray')]
               ]       
      #Agrego la tabla al layout
      layout.extend(tabla)
      window_sopa = sg.Window('Sopa de Letras Educativa',
                size=(ancho * 100, 600),  
                font='Courier', 
                auto_size_text=True,
                text_justification='center',
                background_color='dark slate gray',
                resizable=True).Layout(layout)
      #Diccionario con las coordenadas como clave y el color como dato
      resolucion = {}
      #Cargo el diccionario con al resolucion a la sopa de letras para compararlo con el diccionario progreso.
      for palabra in list(palabras.keys()):
       for coordenada in palabras[palabra]["coord"]:
         resolucion[coordenada]=palabras[palabra]["color"]
      progreso = {}
      while True:
       try:
        evento, values = window_sopa.Read()
        if evento=="revisar":
         try:
          if sorted(progreso) == sorted(resolucion):
           seguir = sg.PopupYesNo("FELICITACIONES, haz ganado! Deseas jugar otra vez?", 
                    font=('Courier', 13, 'bold'),
                    background_color='green',
                    button_color=('white', 'green'),
                    no_titlebar=True) 
           if seguir == 'Yes':
            jugar()
            break
           else:
            break  
          else:
           sg.Popup("Oops! Revisá los errores y seguí intentándolo.", 
            font=('Courier', 13, 'bold'),
            background_color='orange',
            button_color=('white', 'orange'),
            no_titlebar=True)
         except:
          sg.Popup("Oops! Revisá los errores y seguí intentándolo.", font='Courier')
        elif evento == 'help':
          if data['ayuda'][0] == 'si':
            window_sopa.FindElement('lista_pal').Update(values=data['palabras'])
          elif data['ayuda'][0] == 'no' and data['ayuda'][1] == 'no':
            sg.Popup('La ayuda está desactivada, debes intentarlo sólo/a!', 
              font=('Courier', 12, 'bold'), 
              no_titlebar=True,
              grab_anywhere=True,
              background_color='orange',
              button_color=('white', 'orange'))
        elif evento=="lista_pal":
         sg.PopupScrolled(data["definiciones"][str(values["lista_pal"][0])],  
             title=values["lista_pal"][0],
             button_color=('white', 'dark slate gray'))
        elif evento == 'volver':
          break
        elif evento in progreso:
          progreso.pop(evento)
          window_sopa.FindElement(evento).Update(background_color='white')
        elif values["rad_sust"]:
          progreso[evento] = data["colores"]["Sustantivos"]
          window_sopa.FindElement(evento).Update(background_color=data["colores"]["Sustantivos"])
        elif values["rad_verb"]:
          progreso[evento]=data["colores"]["Verbos"]
          window_sopa.FindElement(evento).Update(background_color=data["colores"]["Verbos"])
        elif values["rad_adj"]:
          progreso[evento]=data["colores"]["Adjetivos"]  
          window_sopa.FindElement(evento).Update(background_color=data["colores"]["Adjetivos"])
       except:
        break      
      window_sopa.Close()
    except IndexError:
      sg.Popup('Agrega palabras en la configuración para poder jugar',
        background_color='orange',
        button_color=('white','orange'),
        font=('Courier',13,'bold'),
        no_titlebar=True)
    except TypeError:
      sg.Popup('Agrega palabras en la configuración para poder jugar',
        background_color='orange',
        button_color=('white','orange'),
        font=('Courier',13,'bold'),
        no_titlebar=True)
#-----------------------------------------------------------------------------------------------