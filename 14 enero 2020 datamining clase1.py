#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 13:18:47 2020

@author: alrier
"""
''' TEXT MINING'''
'''with the text i can:
    1. parse text.
    2. identify, find, extract relevant info text.
    3. classify text docs. 
    4. search 4 text docs. 
    5. generate "sentimental analysis", identifying if thers 0 or 1 for some feeling.
    6. topic models. '''


 #'''HANDLING TEXT IN PYTHON:'''

'''It depends of whats u want to do with the document'''

texto1 ="Ethics are built right into the ideas and objetives of the United Nations"
'''este len va a hacer el conteo del total de caracteres que hay que son 73'''
len(texto1)
print(len(texto1))

'''simplemente divido el texto en palabras con un len de 13'''
texto2 = texto1.split()
len(texto2)
print(len(texto2))

'''si lo que se busca es conocer palabras superióres a determinado número de 
caracteres, entonces creo un loop que las busque'''
[a for a in texto2 if len(a)>3]
print([a for a in texto2 if len(a)>3])

''' CApitalization words (palabras en mayúsculas)

cuando deseo buscar todas aquellas palabras que inicien con mayuscula o estén capitalizadas'''
[w for w in texto2 if w.istitle()]
print([w for w in texto2 if w.istitle()])    

'''cuando busco la finalización de una palabra, por ejemplo, la letra s o a'''
[w for w in texto2 if w.endswith('s')]
print([w for w in texto2 if w.endswith('s')])

text3 = "To be or not to be"
'''este conteo me dará 6 por el número de palabras que hay'''
text4 = text3.split()
len(text4)
print(len(text4))

'''este conteo me dará 5, debdido a la palaba "to" que está repetida'''
len(set(text4))
print(len(set(text4)))
'''este comando nos muestra el error de lo que hablabamos arriba, el TO en mayusculas
y el mismo to en minusculas'''
set(text4)
print(set(text4))
'''para arreglar este error, vamos a construír este loop que cambia a minusculas
y que nos regresa el conteo de 4, obviando el "to" porque ya está en minusculas.'''
len(set([w.lower() for w in text4]))
print(len(set([w.lower() for w in text4])))

''' SOME WORD COMPARISON FUNCTIONS'''

'''s.startwith()
s.endswith()
t in s  "para encontrar un determinado strim en algun lugar"

s.isupper(); s.islower(); s.istitle() 
s.isalpha(); s.isdigit(); s.isalnum.'''

'''CLEANING TEXT'''

text8= '  A quick brown fox jumped over the lazy dog. '
text8.split()
print(text8.split())
text9 = text8.strip()
text9.split()
print(text9.split())
print(text9)

                           # '''HANDLING LARGE TEXTS'''
'''read files'''
'''le pido a python que lea la delcaracion de derechos humanos'''
f = open('UNDHR.txt', 'r')
'''le pido que lea la primera linea'''
f.readlines()

'''reading the full file'''
#se debe tener en cuenta que arriba ya crée una variable llamada f que contiene el doc
'''pongo el cursor en el inicio nuevamente'''
f.seek(0)
'''abro una nueva viariable y meto ahí el lector de documentos con mi variable f'''
text12 = f.read()
len(text12)
'''una vez tengo el texto cargado y quiero hacer algunos análisis lo separo'''
texte13 = text12.split()




