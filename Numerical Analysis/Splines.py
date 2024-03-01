# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 10:47:53 2023

@author: marti
"""

import numpy as np
from math import sqrt

def trisol(k,a,c,b):

    l = np.empty(n-1)
    u = np.empty(n)
    u[0]=a[0]

    for i in range(0, k):
        l[i]=c[i]/u[i]
        u[i+1]=a[i+1]-l[i]*c[i]
        
    x[0]=b[0]
    
    for i in range(1,k-1):
        x[i]=b[i]-l[i-1]*x[i-1]
    
    x[k]=x[k]/u[k]
    
    for i in range(k-1,0,-1):
        x[i]=x[i]/u[i]-l[i]*x[i+1]
    
    return x

def spl(t,n,x,y,z,h):
    for i in range(n):
        if t<x[i+1]: break
    s = np.empty()
    # calculate cubic
    s[t]= z[i+1]/(6*h[i])
    return s

iname = 'data1.txt'#input('Nombre del fichero de datos:')
oname = 'nwt_' + iname

data = np.loadtxt(iname, dtype=float)

print(data)

x=data[:,0]
y=data[:,1]
n=len(x)-1
np=256

u=([0,0])
l=([0,0])
h = np.empty(n)
d = np.empty(n)
z = np.empty(n)

for i in range(0,n):
    h[i]=x[i+1]-x[i]
    d[i]=(y[i+1]-y[i])/h[i]

a=([0,0,0,0])
b=([0,0,0,0])
for i in range(1,n):
    a[i]=2*(h[i-1]+h[i])
    b[i]=6*(d[i]-d[i-1])
    
    
trisol(n-2,a,h[1:n-1],b)

z[0]=0
z[n]=0

for l in range(0,np):
    t[l]= x[0]+l[x[n]-x[0]]/np
    f.write(t[l], spl(t,n,x,y,z,h))

    
    
    
    
    
    
    
    
    
    