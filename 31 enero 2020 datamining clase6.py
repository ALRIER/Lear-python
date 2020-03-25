#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 09:35:06 2020

@author: alrier
"""

'''POS TAGGING WITH NLTK'''

'''como sabes si una frase esta compueswta por verbos, pronombres, adjetivos, etc.'''
import nltk
'''con este comando recibimos ayuda de nltk para ver la clase a la que pertenece una abreviación como MD'''
nltk.help.upenn_tagset('MD')
'''agarramos la frase y la tokenizamos'''
text11 = "children shouldn't drink a sudary drink before bed"
text13 = nltk.word_tokenize(text11)
'''una vez tokenizada la ponemos en pos_tag para ver como se compone su conjunto de terminos'''
f = nltk.pos_tag(text13)
print(f)
#output=[('children', 'NNS'), ('should', 'MD'), ("n't", 'RB'), ('drink', 'VB'), ('a', 'DT'), ('sudary', 'JJ'), ('drink', 'NN'), ('before', 'IN'), ('bed', 'NN')]
'''y python nos regresa las palabras que componen la frase con su respectiva abreviación, luego es tan simple como
buscar las referencias con ayuda del comando hepl que se vió arriba'''

