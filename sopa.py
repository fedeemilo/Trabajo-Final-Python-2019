
import PySimpleGUI as sg
import string 
import random
import json
#ARMANDO LA SOPA DE LETRAS
def sopa():
    #sopa de letras
    layout = []
    #creo la estructura que retorna el layout de la sopa de letras y el diccionario de palabras 
    retorno = []
    #creo la estructura que contiene cada palabra con su tipo(vert-horiz) y con una lista donde cada elemento
    #es la coordenada de cada letra de la palabra
    palabras={}
    lista_auxiliar = []

    with open('configuracion.json', encoding='utf-8') as f:
     data = json.load(f)

    cant_sust = int(data['cantidad']['Sustantivos'])
    cant_verb = int(data['cantidad']['Verbos'])
    cant_adj = int(data['cantidad']['Adjetivos'])

    len_lista_sust= len(data['sustantivos'])
    len_lista_adj = len(data['adjetivos'])
    len_lista_verb = len(data['verbos'])

    #SUSTANTIVOS
    #________________________________________________
    if cant_sust != 0 and len_lista_sust != 0:
      if cant_sust < len_lista_sust:
        for i in range(cant_sust):
          lista_auxiliar.append(data['sustantivos'][i])
      else:
        for i in range(len_lista_sust):
          lista_auxiliar.append(data['sustantivos'][i])
    else:
      print('Ningún sustantivo para agregar')
      
    #ADJETIVOS
    #________________________________________________
    if cant_adj != 0 and len_lista_adj != 0:
      if cant_adj < len_lista_adj:
        for i in range(cant_adj):
          lista_auxiliar.append(data['adjetivos'][i])
      else:
        for i in range(len_lista_adj):
          lista_auxiliar.append(data['adjetivos'][i])
    else:
      print('Ningún adjetivo para agregar')

    #VERBOS
    #________________________________________________
    if cant_verb != 0 and len_lista_verb != 0:
      if cant_verb < len_lista_sust:
        for i in range(cant_verb):
          lista_auxiliar.append(data['verbos'][i])
      else:
        for i in range(len_lista_verb):
          lista_auxiliar.append(data['verbos'][i])
    else:
      print('Ningún verbo para agregar')
    #________________________________________________
    

    print(lista_auxiliar)
    print(len(lista_auxiliar))

    conjunto_lista_aux = set(lista_auxiliar)
    conjunto_lista_orig = set(data['palabras'])

    print(conjunto_lista_aux)
    print(conjunto_lista_orig)

    resultado_lista = sorted(list(conjunto_lista_aux & conjunto_lista_orig), 
                        reverse=True,
                        key= lambda pal: len(pal))

    data['palabras'] = resultado_lista.copy()
    print(data['palabras'])

    if data["orientacion"] =="Horizontal":
      #en la matriz mxn si elige HORIZONTAL m = cantidad palabras y n = len(palabra+grande)
      #m = filas 
      #n = columnas
      m = len(data["palabras"])
      n = len(data["palabras"][0])      
    else:
      #si es vertical es al revés
      m = len(data["palabras"][0])
      n = len(data["palabras"])
    #creo las filas del layout que representa a la sopa de letras
    for i in range(m):
      layout.append([])
    #coordenadas del resto de caracteres
    coor=[]
    if data["orientacion"] == "Horizontal":
     #cargo en la variable azar la cantidad de palabras de la configuración 
     azar = []
     for cant_words_h in range(m):
      azar.append(cant_words_h)

     
     #comienzo el llenado del layout de la sopa 
     for fila in range(m):
      num_azar_h = random.choice(azar)
      azar.remove(num_azar_h)
      #cargo en word la palabra que se encuentra en la posicion num_azar
      word = data["palabras"][num_azar_h]
      #creo la estructura de las palabras como un diccionario con su color y una lista
      # de las coordenadas de las letras
      palabras[word] = {}
      if word in data["sustantivos"]:
        palabras[word]["color"] = data["colores"]["Sustantivos"]
      elif word in data["verbos"]:
        palabras[word]["color"] = data["colores"]["Verbos"]
      else:
        palabras[word]["color"] = data["colores"]["Adjetivos"] 
      palabras[word]["coord"] = []
      #num representa el indice de inicio en la fila de la palabra de forma random
      num = random.randint(0,(n-len(word)))
      #cargo el layout con letras random en la fila correspondiente con una cantidad num
      #el primer for representa la carga de letras previas a las letras de la palabra
      for col_letra_previa in range(num):
       layout[fila].append(sg.T(random.choice(string.ascii_lowercase), 
                            text_color="black",
                            size=(7,2), 
                            background_color='white', 
                            pad=(0.5,0.5), 
                            key=(fila,col_letra_previa) , 
                            justification='center' , 
                            click_submits=True, 
                            enable_events=True))     
       coor.append((fila,col_letra_previa))
      #el segundo for representa el llenado de las letras de la palabra
      for col_letra_word in range(len(word)):
       layout[fila].append(sg.T(word[col_letra_word], 
                            text_color="black",
                            size=(7,2), 
                            background_color='white', 
                            pad=(0.5,0.5), 
                            justification='center', 
                            key=(fila,num+col_letra_word) , 
                            click_submits=True, 
                            enable_events=True))
       palabras[word]["coord"].append((fila,num+col_letra_word))
      #el tercer for representa la carga de letras posterior a las letras de la palabra
      for col_letra_posterior in range(n-len(word)-num):
       layout[fila].append(sg.T(random.choice(string.ascii_lowercase), 
                            text_color="black",
                            size=(7,2), 
                            background_color='white', 
                            pad=(0.5,0.5), 
                            key=(fila,num+len(word)+col_letra_posterior), 
                            justification='center', 
                            click_submits=True, 
                            enable_events=True))
       coor.append((fila,num+len(word)+col_letra_posterior))
     #en layout voy cargando las filas para crear la sopa de letras
     retorno.append(layout)
     #en palabras voy cargando cada palabra con su color y sus coordenadasde ubicación
     retorno.append(palabras)
     retorno.append(coor)
     return retorno
    else:
      #en la matriz mxn si elige VERTICAL m = len(palabra+grande) y n = cantidad de palabras
     azar = []
     for cant_words_v in range(n):
      azar.append(cant_words_v)
     for columna in range(n):
      num_azar_v = random.choice(azar)
      azar.remove(num_azar_v)
      word = data["palabras"][num_azar_v]
      palabras[word] = {}
      if word in data ["sustantivos"]:
        palabras[word]["color"] = data["colores"]["Sustantivos"]
      elif word in data ["verbos"]:
        palabras[word]["color"] = data["colores"]["Verbos"]
      else:
        palabras[word]["color"] = data["colores"]["Adjetivos"] 
      palabras[word]["coord"] = []
      num = random.randint(0,(m-len(word)))

      letras_abecedario = ''

      #en letras_abecedario guardo un string con las letras del abecedario
      #en minúsculas o mayúsculas dependiendo como esté seteado en la condiguración
      if data['mayus'] == 'Mayúsculas':
        letras_abecedario = string.ascii_uppercase
      else:
        letras_abecedario = string.ascii_lowercase

      for fil_letra_previa in range(num):
        layout[fil_letra_previa].append(sg.T(random.choice(letras_abecedario), 
                          text_color="black",
                          size=(7,2), 
                          background_color='white', 
                          pad=(0.5,0.5), 
                          key=(fil_letra_previa,columna),
                          justification='center',  
                          click_submits=True, 
                          enable_events=True))
        coor.append((fil_letra_previa,columna))
      for fil_letra_word in range(len(word)):
        #guardo la letra de la palabra a encontrar en una variable 
        #para convertirla en mayúscula si es que así está seteado en la configuración
        letra = word[fil_letra_word]
        if data['mayus'] == 'Mayúsculas':
          letra = letra.upper()

        layout[fil_letra_word+num].append(sg.T(letra, size=(7,2), 
                          text_color="black",
                          background_color='white', 
                          pad=(0.5,0.5), 
                          justification='center', 
                          key=(fil_letra_word+num,columna) , 
                          click_submits=True, 
                          enable_events=True))
        palabras[word]["coord"].append((fil_letra_word+num,columna))
      for fil_letra_posterior in range(num+len(word),m):
        layout[fil_letra_posterior].append(sg.T(random.choice(letras_abecedario), 
                          text_color="black",
                          size=(7,2), 
                          background_color='white', 
                          pad=(0.5,0.5), 
                          key=(fil_letra_posterior+num+len(word),columna),
                          justification='center', 
                          click_submits=True, 
                          enable_events=True)) 
        coor.append((fil_letra_posterior+num+len(word),columna))
     retorno.append(layout)
     retorno.append(palabras)
     retorno.append(coor)
     return retorno  
#-----------------------------------------------------------------------------------------------
