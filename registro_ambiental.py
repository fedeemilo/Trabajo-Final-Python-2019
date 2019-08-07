import os
import json
import time
import Adafruit_DHT
##############################################################################################
#Creo una clase que tiene una funcion que obtiene temperatura/humedad y la devuelve como diccionario.
class Temperatura_Humedad:
    def __init__(self, pin=17, sensor=Adafruit_DHT.DHT11):
        # Usamos el DHT11 que es compatible con el DHT12
        # en caso de usar el 22 Adafruit_DHT.DHT22
        self._sensor = sensor
        self._data_pin = pin

    def datos_sensor(self):
        humedad, temperatura = Adafruit_DHT.read_retry(self._sensor, self._data_pin)
        return {'temperatura': temperatura, 'humedad': humedad}
##############################################################################################
#Creo un objeto de la clase ya mencionada.
objeto = Temperatura_Humedad()
##############################################################################################
#La funcion llama al objeto creado para obtener la informacion y colocarla en la variable "informacion", ademas se le coloca la fecha de registro.
def leer_informacion():
    informacion= Temperatura_Humedad.datos_sensor()
    informacion.update({"fecha": time.asctime(time.localtime(time.time()))})
    return informacion
############################################################################################## 
#La funcion guarda los datos obtenidos por info en el archivo json "datos_oficinas.json" , si se encuentra vacio crea la lista para llenarla con los datos.
def guardar_informacion(info,num):
    with open('datos_oficinas.json', "r") as archivo:
        try:
            datos_registro = json.load(archivo)
        except Exception:
            datos_registro = {}
    try
        datos_registro["oficina"+str(num)].append(info)
    except Exception:
        datos_registro["oficina"+str(num)]=[info]
    with open(datos_oficinas.json, "w") as archivo:
        json.dump(datos_registro, archivo, indent=4)
##############################################################################################
#Primero se selecciona en que oficina se encuentra.
#Luego ,cada  1 minuto se obtiene datos y se lo colocan en el archivo json "datos_oficinas.json" 
if __name__ == "__main__":
	num = input("¿En que oficina se encuentra?(sólo el número)")
    while True:
        dato =leer_informacion()
        guardar_informacion(dato,num)
        time.sleep(60) 