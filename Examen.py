# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 09:18:33 2019

@author: DELL
"""

import numpy as np
import pandas as pd
# 1

vector=np.array(np.zeros((10), dtype=int))
print(vector)

# 2

zeros_vec_v2 = np.zeros(10)
zeros_vec_v2[5]=1
zeros_vec_v2

# 3
vector_cincuenta = list(range(50))
vector_cincuenta.reverse() 
vector_cincuenta
# 4 Cambiar el orden de un vector de 50 elementos, el de la posicion 1 es el de la 50 etc.

numeros = np.arange(50)**1
print(numeros)
numeros.shape
print(numeros.shape)
cs=np.transpose(numeros)
print(cs)
# 5  Crear una matriz de 3 x 3 con valores del cero al 8
matriz = np.random.randint(0, 8, size=(3, 3))
print(matriz)
# 6  Encontrar los indices que no sean cero en un arreglo

arreglo = [1,2,0,0,4,0]
arreglo_noceros=np.nonzero(arreglo)
print(arreglo_noceros)

# 7 Crear una matriz de identidad 3 x 3
matrizId=np.identity(3)

print(matrizId)

# 8 Crear una matriz 3 x 3 x 3 con valores randomicos
matrizRamd=np.random.rand(3,3)
print(matrizRamd)
# 9 Crear una matriz 10 x 10 y encontrar el mayor y el menor
matrizRamd=np.random.rand(10,10)
max=np.max(matrizRamd)
min=np.min(matrizRamd)
print(matrizRamd)
print(max)
print(min)
# 10  Sacar los colores RGB unicos en una imagen (cuales rgb existen ej: 0, 0, 0 - 255,255,255 -> 2 colores)


#¿Como crear una serie de una lista, diccionario o arreglo?

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))



series = pd.Series(mylist)
print('Series:')
print(series)
series = pd.Series(myarr)
print('Series:')
print(series)
series = pd.Series(mydict)
print('Series:')
print(series)
#12 Como convertir el indice de una serie en una columna de un DataFrame?
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict) 
df = pd.DataFrame(ser)
print('DataFrame:')
print(df)
# Transformar la serie en dataframe y hacer una columna indice
#13 ¿Como combinar varias series para hacer un DataFrame?

ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df2 = pd.DataFrame(ser1,ser2)
print('DataFrame:')
print(df2)
df3 = pd.DataFrame(df2)
print('DataFrame:')
print(df3)
#14 ¿Como obtener los items que esten en una serie A y no en una serie B?
ser11 = pd.Series([1, 2, 3, 4, 5])
ser22 = pd.Series([4, 5, 6, 7, 8])
comun_value = set(ser1).intersection(set(ser2))
print(comun_value)
values = ser11.append(ser22)
values = set(values)
#15) ¿Como obtener los items que no son comunes en una serie A y serie B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

comun_values = set(ser1).intersection(set(ser2))
print(comun_value)
values = ser11.append(ser22)
values = set(values)
#16) ¿Como obtener el numero de veces que se repite un valor en una serie?
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
print(ser)
#17) ¿Como mantener los 2 valores mas repetidos de una serie, y a los demas valores cambiarles por 0 ?
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
np.random.RandomState(100)

ser = pd.Series(np.random.randint(1, 5, [12]))
print(ser)

#18) ¿Como transformar una serie de un arreglo de numpy a un DataFrame con un shape definido?
ser = pd.Series(np.random.randint(1, 10, 35))
shape(7,5)
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))

pos = [0, 4, 8, 14, 20]
print(ser)
#19) ¿Obtener los valores de una serie conociendo la posicion por indice?
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u
#20) ¿Como anadir series vertical u horizontalmente a un DataFrame?
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
ser1 = pd.Series(range(5))

ser2 = pd.Series(list('abcde'))
#21)¿Obtener la media de una serie agrupada por otra serie?
#groupby tambien esta disponible en series.

frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
print(pesos.tolist())
print(frutas.tolist())




#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']

# Los valores van a cambiar por ser random
# apple     6.0
# banana    4.0
# carrot    5.8
# dtype: float64


frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))

pesos = pd.Series(np.linspace(1, 10, 10))

print(pesos.tolist())

print(frutas.tolist())
#22)¿Como importar solo columnas especificas de un archivo csv?
#https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv.




url = 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'
df = pd.read_csv(url,usecols=["crim","zn","indus","chas"])
df.head()



