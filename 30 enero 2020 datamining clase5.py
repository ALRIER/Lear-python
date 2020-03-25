# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''normalization and stemming'''

input1 = "List Listed lists listing listings"
words = input1.lower().split()
print(words)
#output = ['list', 'listed', 'lists', 'listing', 'listings']


'''STEAMMING'''
'''steamming is to find the root word or form of any given word'''

import nltk

'''aquí el programa va a imprimir las racies de toda la lista de palabras llamada word'''
porter = nltk.PorterStemmer()
a = [porter.stem(t) for t in words]
print(a) 
#outrput =['list', 'list', 'list', 'list', 'list'] me regresa este output debido a que todas las palabras estan iniciand con "list"

'''LEMMATIZATION'''
'''es una variante de el steamming, pero acá lo que se busca es obtener una lista de palabras significativas'''

udhr = nltk.corpus.udhr.words('English-Latin1')
print(udhr[:20])
#output =['Universal', 'Declaration', 'of', 'Human', 'Rights', 'Preamble', 'Whereas', 'recognition', 'of', 'the', 'inherent', 'dignity', 'and', 'of', 'the', 'equal', 'and', 'inalienable', 'rights', 'of']
b = [porter.stem(t)for t in udhr [:20]]
print(b)
 #output=['univers', 'declar', 'of', 'human', 'right', 'preambl', 'wherea', 'recognit', 'of', 'the', 'inher', 'digniti', 'and', 'of', 'the', 'equal', 'and', 'inalien', 'right', 'of']
'''Se puede observar como los outputs son diferentes yq eu extrae los caracteres raíz de las palabras, sin embargo los resultados obtenidos son palabras sin sentido, para eso se suele usar el lemmatization que tra las raices pero con sentido'''
WNlemma = nltk.WordNetLemmatizer()
c= [WNlemma.lemmatize(t) for t in udhr[:20]]
print(c)
#output= ['Universal', 'Declaration', 'of', 'Human', 'Rights', 'Preamble', 'Whereas', 'recognition', 'of', 'the', 'inherent', 'dignity', 'and', 'of', 'the', 'equal', 'and', 'inalienable', 'right', 'of'] 


