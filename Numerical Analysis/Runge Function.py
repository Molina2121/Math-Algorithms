# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 20:22:18 2023

@author: marti
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from math import pi,exp,sqrt

# Cálculo de la diferencia dividida
def difdiv(n,x,y):
    d=np.zeros((n+1,n+1))
    for i in range(0,n+1):
        d[i,0]=y[i]
    for k in range(1,n+1):
        r=0
        for i in range(0, n-k+1):
            if (x[i]==x[k+i]):
                d[i,k]=y[i+k-r]/math.factorial(k)
                r+=1
            else:
                d[i,k]=(d[i+1,k-1]-d[i-r,k-1])/(x[i+k]-x[i])
                r=0
    return d

# Fórmula de Newton
def nwt(t,n,x,d):
    
    p=d[0,n]
    for k in range(n-1,-1,-1):
        p=d[0,k]+(t-x[k])*p
    
    return p



num_puntos = 256
a, b = -1, 1
n=3
x=np.zeros(n+1)

for i in range(0,n+1):
    x[i] = (1/2)*(a+b-(a-b)*math.cos(((2*i+1)/(2*n+2))*math.pi))
    print (x[i])
    
def f(x):
    return (1.0/(sqrt(2*pi)))

y = f(x)


t = np.linspace(a, b, num_puntos + 1)
d = difdiv(n, x, y)
p = np.zeros(num_puntos + 1)

for l in range(num_puntos + 1):
    p[l] = nwt(t[l], n, x, d)

plt.plot(t, p)
