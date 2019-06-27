
from pattern.es import verbs, tag, spelling, lexicon

def clasificar(palabra):
  palabra_tag = tag(palabra, tokenize=True, encoding='utf-8')

  if not palabra.lower() in verbs:
    if not palabra.lower() in spelling:
      if (not(palabra.lower() in lexicon) and not(palabra.upper() in lexicon) and not(palabra.capitalize() in lexicon)):
        return False
      else:
        return palabra_tag
    else:
      return palabra_tag
  else:
    return palabra_tag

#-----------------------------------------------------------------------------------------------
