# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nltk
'''con este comando descargo los libros y archivos de nltk'''
nltk.download()
'''importo los documentos'''
from nltk.book import *
'''llamo el texto que deseo imprimir'''
print(text1)
print(sent1, sent2, sent3)

'''procedo a imprimir el texto 7 y fease 7'''
print(text7)
print(sent7)
print(len(sent7))
'''aqui veo el total de palabras del texto'''
print(len(text7))
'''pero aquí veo el total de palabras unicas del texto, que son solamente 12408'''
print(len(set(text7)))
'''para identificar las primeros 10 unicas alfanuméricos (no repetidas) y 
automaticamente ýthon traerá la impresión de las 10 primeros alfanumericos no repetidas.'''
print(list(set(text7)) [:10])
'''para el conteo de frecuencia de palabras, automáticamente python va a generar la 
DISTRIBUCIÓN DE FRECUENCIA para este conjunto de datos diciendo que hay 
12408 muestras y 100676 resultados'''
dist = FreqDist(text7)
print(dist)
'''pero como previamente ya creamos un objeto llamado dist que contiene la función de 
frecuencia, pues ahora se puede sacar la longitud del objeto y otras cosas'''
print(len(dist))
'''tambien se puede crear un nuevo objeto que se llame vocab1 y sacar las 10 primeras palabras'''
vocab1 = dist.keys()
vocab1[:10]
print(vocab1)