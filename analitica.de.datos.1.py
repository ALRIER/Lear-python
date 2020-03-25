#import pandas as pd
#ruta = "/Users/User/Downloads/train.csv" #con este comando defino un objeto que se llama ruta que 
#posee por cualidad la ruta que voy a trabajar de acá en adelante
#df = pd.read_csv (ruta) #ojo al lugar donde estara guardado el archivo
#print (df) #imprimo
#df.head()#imprimir cabecera de la lista de datos. 
#df.tail()#imprimir los ultimos datos del conjunto. 
#df.columns()#ayuda a cambiar la cabecera de la lista de datos para lo cual en la parte de abajo
#cabecera = ["ID", "Sobreviviente", "Clase", "Nombre", "Sexo", "Edad", "Hermanos", "Hijos", "Ticket", "Tarifa", "Cabina", "embarque"] #creo un nuevo argumento con
#los nombres de las nuevas variables de la cabecera
#df.columns = cabecera #Luego remplazo el objeto "cabecera" que ya creé por y que contiene
#los nuevos datos de la cabecera. 

#print (df) #imprimo para rectificar. 
#df.to_csv (ruta) #defino el archivo con la ruta donde se van a guardar los cambios realizados
#es importante tener en cuenta que después de realizado este proceso ya no se puede
#cambiar nuevamente los datos porque quedarán guardados en el nuevo archivo. 

#DE AHORA EN ADELANTE TODO ESTA BASADO EN ANALITICA DE DATOS
#generalmente los machine learning aceptan solamente datos enteros, por lo que es bueno convertir los datos. 


#print (df.dtypes) #este comando regresa el tipo de datos que hay, pero debes siempre imprimirlo, sino no va a aparecer. 
#este tipo de comando permite identificar si los datos son objetos, floats, o de qué tipo de datos son y así verificar que tipo de cambios 
#requiere la base de datos que se va a trabajar. 
#print (df.describe()) #este comando me muestra los datos de carácter estadistico y así poder ver si hay algun error a nivel numérico
#este comando puede incluir todos los elementos con el comando (include= "all") en cuyo caso la función quedaría:
#print (df.describe(include="all")) #pero en este caso apareceran varios valores con NAN (no es un númeo), caso en el que el analisis de igual forma no podría llevarse a cabo

#___________________________________________________________________________________________________________________________________________________________________________

#cuando hay datos perdidos que hacer?... el caso de los NAN (no es un número) o interrogantes "#" o demás signos de ausencia de datos. 

#METODO FROPNA (eliminar todo un espacio de datos)
#axis = 0 para elminar filas
#axis = 1 para eliminar columnas

#si quisiera eliminar la fila de "cabina" por ejemplo, hago el comando 
#df.dropna = ("cabina"), axis = 0 esto eliminará toda la fila
#en el caso de una columna hago lo mismo
#al final si deseo implementar el comando a los datos aplico todo igual y agrego inplace = True (). 
#df.dropna(subset = ("cabina"), axis = 0, inplace = True) y posteriór a esto los datos quedarán eliminados. 

#___________________________________________________________________________________________________________________________________________________________________________

#remplazar datos perdidos
#replace()
#PARA EL CASO EDAD (1. calculamos el promedio de edad de toda la columna df. ("edad"). mean () que me da = 29.6, yo redondeo a 30 e implanto el 30 en datos faltantes)
#df("edad").replace(np.nan, promedio) => donde np.nan es el valor a remplazar, en este caso los NAN y promedio es el promedio que obtuve de datos en este caso 30
#antes de hacer el remplazo, primero tengo que llamar a la librería NUNPY 
#import numpy as np
#promedio = 30
#df["Edad"].replace(np.nan, promedio) 
#print (df["Edad"].replace(np.nan, promedio))

#____________________________________________________________________________________________________________________________________________
#CAMBIO DE FORMATO Y CATEGORÍA

#pd.get_dummies
#print (pd.get_dummies (df, columns = ["Sexo"], drop_first = True)) #el drop_first aplica unicamente en lcaso de querer unir dos columnas en 1
#en muchas opcaiones ese espacio de drop_first =True no sirve, el resto es para cambiar un formato. 


#___________________________________________________________________________________________________________________________________________
#AGRUPACION DE DATOS EN CATEGORIAS: 
# se crearán varios grupos: de 0-5 de 6-12 de 13-18 de 19-35 de 36-60 de 61-100
#el comando a usar es pd.cut
#creamos una variable llamada bins
#bins= [0,5,12,18,35,60,100] #aquí ubicamos los rangos de dadades donde finaliza cada rango y el programa entiende los rangos
#names = ["1","2","3","4","5","6"] #este es el nombre numerico de cada rango
#posteriórmente asigno la formula 
#df["Edad"] = pd.cut(df["Edad"], bins, labels = names)
#print (df["Edad"])

#_______________________________________________________________________________________________________________________________________
#VISUALIZACIÓN DE DATOS & PLOTEO DE DATOS

#librerías usadas. 
#1. matplotlib: la más antigua. 
#2. seaborn: se integra muy bn con pandas. 
#3. bokeh: principalmente para web, genera gráficos interactivos para la web. 
#4. pygal: genera grafios vectoriales para pocos datos. 
#5. plotly: principalmente en linea, entorno visual y de aplicación interactiva. 