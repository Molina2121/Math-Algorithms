# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 18:34:15 2023

@author: marti
"""

import numpy as np
import matplotlib.pyplot as plt
import math

x = ([0,0.9511,-0.9511,0.5878,-0.5878])
n=len(x)

a = x.copy() #Copia del conjunto X para ir modificando y conservar X
i = np.argmax(a) #Índice en el que está el máximo de a
xleja   = np.array(a[i]) #Primer elemento del orden de Leja
a = np.delete(a,i) #Quitamos el elemento que ya hemos utilizado
i = np.argmin(a) #Índice en el que está el mínimo de a
xleja = np.append(xleja, a[i]) #Añadimos el segundo elemento
a = np.delete(a,i) #Quitamos el elemento que ya hemos utilizado

j=n-2

g =([])
r=2

while len(a) > 1: 

    for i in range(0,j):
        c=1
        for k in range(0,r):   
            c*= abs(a[i]-xleja[k])
        g = np.append(g, c)
            
    m = np.argmax(g) 
    xleja = np.append(xleja, a[m])
    a = np.delete(a,m)
    
    for q in range(0,j):
        g = np.delete(g,0)

    j-=1
    r+=1
    
xleja = np.append(xleja, a[0])    

print(xleja)
