from pattern.web import Wiktionary, plaintext
from pattern.es import verbs, tag, spelling, lexicon
from functools import lru_cache
import PySimpleGUI as sg

@lru_cache(maxsize=16)
def clasificar_wikt(palabra='casa'):
	clasif = '_no_sabe_'
	sustantivo = 'NN'
	adjetivo = 'JJ'
	verbo = 'VB'

	for i in range(100000):
		sg.PopupAnimated(sg.DEFAULT_BASE64_LOADING_GIF, 
			background_color='white', 
			time_between_frames=100,
			location=(610,183))
	engine = Wiktionary(language="es")
	articulo = engine.search(palabra)
	sg.PopupAnimated(None)

	if articulo != None: 
		pos_inicial = articulo.source.find('<dt>')
		pos_final = articulo.source.find('<dt>', pos_inicial + 1)
		hasta_punto = plaintext(articulo.source[pos_inicial:pos_final]).find('.')
		definicion = plaintext(articulo.source[pos_inicial:pos_final])

		print('\n  Def: *', definicion, '*',sep='')

		if ('ES:Sustantivos' in articulo.categories):
			print('Es un sustantivo según Wiktionary')				
			return [palabra, definicion, sustantivo]
		if ('ES:Adjetivos' in articulo.categories):
			print('Es un adjetivo según Wiktionary')			
			return [palabra, definicion, adjetivo]
		if ('ES:Verbos' in articulo.categories):
			print('Es un verbo según Wiktionary')
			return [palabra, definicion, verbo]
		if clasif == '_no_sabe_':
			print('Wiktionary no pudo clasificar la palabra')
			return [palabra, definicion, clasif]
	else: 
		print('La palabra no se encuentra en Wiktionary')		
		return False


@lru_cache()
def clasificar_pattern(palabra='casa'):
  palabra_tag = tag(palabra, tokenize=True, encoding='utf-8')
  print(palabra_tag)

  if not palabra.lower() in verbs:
    if not palabra.lower() in spelling:
      if (not(palabra.lower() in lexicon) and not(palabra.upper() in lexicon) and not(palabra.capitalize() in lexicon)):
        print('La palabra no se encuentra en pattern.es')
        return False
      else: 
        return palabra_tag
    else:
      return palabra_tag
  else:
    return palabra_tag

