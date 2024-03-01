# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 20:09:21 2023

@author: marti
"""
import numpy as np
import matplotlib.pyplot as plt
import math

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

iname = input('Nombre del fichero de datos:')
oname = 'nwt_' + iname

data = np.loadtxt(iname, dtype=float)

print(data)

x=data[:,0]
y=data[:,1]
n=len(x)-1


num=256
a=min(x[:])
b=max(x[:])
t=np.linspace(a,b,num+1)

d=difdiv(n,x,y)

p=np.zeros(num+1)

with open(oname,'w')as f:
    for l in range(num+1):
        p[l]=nwt(t[l],n,x,d)
        f.write(str(t[l])+' '+str(p[l])+'\n')

plt.plot(t,p)