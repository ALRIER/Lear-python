#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 09:22:16 2020

@author: alrier
"""
import nltk

'''ahora pasamos a la tokenización'''

text11 = "children shouldn't drink a sudary drink before bed"
print(text11.split())
#output = ['children', "shouldn't", 'drink', 'a', 'sudary', 'drink', 'before', 'bed']
''' para un total de 8 palabras'''
p= nltk.word_tokenize(text11)
print(p)
#output = ['children', 'should', "n't", 'drink', 'a', 'sudary', 'drink', 'before', 'bed']
d1= [nltk.word_tokenize(t) for t in text11]
print(d1)
#output= [['c'], ['h'], ['i'], ['l'], ['d'], ['r'], ['e'], ['n'], [], ['s'], ['h'], ['o'], ['u'], ['l'], ['d'], ['n'], ["'"], ['t'], [], ['d'], ['r'], ['i'], ['n'], ['k'], [], ['a'], [], ['s'], ['u'], ['d'], ['a'], ['r'], ['y'], [], ['d'], ['r'], ['i'], ['n'], ['k'], [], ['b'], ['e'], ['f'], ['o'], ['r'], ['e'], [], ['b'], ['e'], ['d']]

'''como se puede observar cada uno de los comandos dicta un resultado diferente en el primero me brinda el comando tokenizado
de cada palabra y separa el should y la n't por separado y en el segundo me brinda la tokenización del total de caracteres usados'''
