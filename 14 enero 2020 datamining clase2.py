#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:24:21 2020

@author: alrier
"""


'''Aplicación al entorno real.'''

'''en un tweet cuando tenemos texto incrustado con signos podemos llamar un loop que 
se encargué de retirar los signos de las palabras'''

tweet = ' "Ethics are built right into the ideals and objectives of the United Nations" #UNSG @NYSociety for Ethical Culture bit.ly/2guVelr @UN @UN_Women '

print([word for word in tweet.split() if word.statswith('#', '@')])

'''FIND SPECIFIC WORDS'''

'''HASHTAGS'''
[w for w in tweet if w.startswith('#')]

'''callouts'''
[w for w in tweet if w.startswith('@')]

'''Como es usual los @ no tienen espacios, por loq ue es bueno intentar un nuevo modelo de busquera'''
'''este comando le dice a python que haga una busqueda de atras hacia adelante de todos 
los caracteres que tengan de la A a la Z y del 0 al 9 incluida la _, que además, esten junto con
un @ en su sintaxis''' 
[w for w in tweet if re.search ('@ [A-Za-z0-9_]+', w)]

 '''theres a lot of signs that u can use in the python programmation, for example'''
 
'''. = es un comodin que coincide con un solo caracter. 
^ = comenzar una cadena. 
$ = finaliza la cadena.
[] = matches one of the caracteres that are readen into this. 
[^abc] = uno de los caracteres que no sea a, b o c.
\b = marca el límite de palabras. 
\t = tabulación. 
\d = marcar cualquier digito de 0-9.
\D = cualquier digito que no sea [^0-9]
\s = cualquier espacio en blanco equivalente a [ \t\n\r\f\v]
\w = cualquier coincidencia con alfanuméricos. [a-zA-Z0-9_]
\W = cualquier cosa que no sea un alfanumérico. [^a-zA-Z0-9_]

Tambien hay repeticiones. 

* = concordancias de cero o mas ocurrencias.
+ = debe ocurrir al menos 1 ves, pero de ahí en adelante. 
? = 0 o 1 ocurrencias. 
{n} = exactamente n numero de repeticiones. 
{n,} = al menos n numero de repeticiones. 
{ ,n} = como maximo o a lo sumo n numero de repeticiones. 
{m,n} = al menos m numero de repeticiones y no más de n numero de repeticiones. 

Ahora bien... esta expresión, se puede resumir en:
    [w for w in tweet if re.search ('@ [A-Za-z0-9_]+', w)]
    [w for w in tweet if re.search ('@ \w+', w)]
    
                    Tiempos. 
                    
                    