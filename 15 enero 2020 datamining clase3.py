#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 13:34:17 2020

@author: alrier
"""


import pandas as pd

time_sentences = ["Monday: The doctor's appointment is at 2:45pm.", 
                  "Tuesday: The dentist's appointment is at 11:30 am.",
                  "Wednesday: At 7:00pm, there is a basketball game!",
                  "Thursday: Be back home by 11:15 pm at the latest.",
                  "Friday: Take the train at 08:10 am, arrive at 09:00am."]
'''organizo mi objeto como un dataframe con texto'''
df = pd.DataFrame(time_sentences, columns=['text'])
print(df)

'''usando este comando puedo contabilizar el numero de caracteres para 
esta cadena de texto, indicasndome para cada renglon el total de caracteres.'''
df ['text'].str.len()
print (df ['text'].str.len())

#'''además puedo usar el comando str.split().str.len() para encontrar el número de tokens que compone toda la cadena de comandos.''''

df ['text'].str.split().str.len()
print (df ['text'].str.split().str.len())

'''tambien Usando str.count, podemos contar las ocurrencias de un patrón 
en cada cadena de la serie. '''
df['text'].str.contains('appointment')
print(df['text'].str.contains('appointment'))

'''este comando genera un conteo de los digitos que hay en un sting'''
df['text'].str.count(r'\d')
print(df['text'].str.count(r'\d'))

'''este comando encuentra la candidad de ocurrencias en una cadena'''
df['text'].str.findall(r'\d')
print(df['text'].str.findall(r'\d'))

