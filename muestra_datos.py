import time
from itertools import repeat
from luma.core import legacy
### MATRIZ
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT,TINY_FONT, SINCLAIR_FONT, LCD_FONT
### MIC
import RPi.GPIO as GPIO
#para emular
from demo_opts import get_device
class Matriz:
	def __init__(self, numero_matrices = 1, orientacion = 0, rotacion = 0, ancho = 8, alto = 8):
		self.font = [CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT]
		self.serial = spi(port=0, device=0, gpio=noop())
		self.device = max7219(self.serial, width = ancho, height = alto, cascaded = numero_matrices, rotate = rotacion)
	def mostrar_mensaje(self, msg, delay=0.1, font=1):
		show_message(self.device, msg, fill = 'white', font = proportional(self.font[font]), scroll_delay=delay)


class Sonido:
    def __init__(self, canal=22):
         """Init para la configuración del mic"""
            self._canal = canal
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self._canal, GPIO.IN)
         # Desactivo las warnings por tener más de un circuito en la GPIO
            GPIO.setwarnings(False)
            GPIO.add_event_detect(self._canal, GPIO.RISING)

    def evento_detectado(self, mostrarM):
         """Si se detecta un sonido (aplauso) se muestran los datos de temperatura y humedad en la matriz"""
            if GPIO.event_detected(self._canal):
                mostrarM()
         

def mostrarEnMatriz(emu):
"""Módulo para mostrar los datos de temperatura y humedad en la matriz"""
    #si el dispositivo es un emulador
	if emu: #para emular pido el device
		device = get_device()
		datos = {'temperatura':34, 'humedad':89}
	else:
		#Inicializar la matriz: identificar puerto
		serial = spi(port = 0, device = 0, gpio = noop())
		#crear una insctancia del objeto (matriz)
		device = max7219(serial, cascaded = 2, block_orientation = 0)
    
    #abro el archivo datos_oficinas creado en la app registro_ambiental y guardo
    #el último registro de temperatura y humedad registrado en el número de 
    # oficina que ingresó el usuario
    with open('datos_oficinas.json', "r") as archivo:
        try:
            datos_registro = json.load(archivo)

    temp = datos_registro["oficina"+str(num)][len(datos_registro["oficina"+str(num)])]["temperatura"]
    hum = datos_registro["oficina"+str(num)][len(datos_registro["oficina"+str(num)])]["humedad"]

	temp = datos['temperatura']
	hum = datos['humedad']
    #--------------------------------------------------------------------------------------
    #muestro primero la palabra Temperatura y luego con un delay 
    msg = 'Temperatura'
	show_message(device, msg, fill='white', font=proportional(LCD_FONT), scroll_delay=0.05)
	msg = str(temp)+'º C'
	with canvas(device) as draw:
		text(draw, (1, 0), msg, fill="white")
	time.sleep(3)
	msg = 'Humedad'
	show_message(device, msg, fill='white', font=proportional(LCD_FONT), scroll_delay=0.05)
	msg = str(hum)+'%'
	with canvas(device) as draw:
		text(draw, (1, 0), msg, fill="white")
	time.sleep(3)
    #--------------------------------------------------------------------------------------
def main():
    emu = input('Está emulando? (y or n): ').lower() in ('s','y','si','yes')
    #emu = True
    if emu:
        mostrarEnMatriz(emu)
    else:
        iniciar_sensores()
        sonido = Sonido()
        while True:
            time.sleep(0.0001)
            sonido.evento_detectado(mostrarEnMatriz)             
    #--------------------------------------------------------------------------------------
if __name__ == "__main__":
  num=input("¿En que oficina se encuentra?(el numero solamente)")
  try:
   main()
  except KeyboardInterrupt:
    pass #no hacer nada              













