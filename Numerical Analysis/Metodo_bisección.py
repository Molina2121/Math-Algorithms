#Metodo de biseccion

from pylab import *
from scipy import *
from math  import ceil #ceil es el techo superior y floor el inferior


#Definir una función; la que me den

def f(x):
    if problema==1:
        f=sin(x)-x**2*exp(-log(x+3))+1
    elif problema==2:
        f=exp(x)-13*x**2
    elif problema==6:
        f=[4*(x[0]-3)**2+3*(x[1]-1)**2-96,log(x[0]-2)-1-cos(x[0]/2+2)]

    return f

problema=1

#intervalo en que se encuentra la raiz, mas pequeño implica mas precision... si es posible geogebra o ptos corte

if problema==1:
    a=-10   #acuerdate de poner a<b
    b=2
elif problema==2:
    a=0
    b=1
elif problema==6:
    a=-3
    b=0
    
#f(a)*f(b) negativo

tolabs=1.e-8
itmax=ceil(-1+log((b-a)/tolabs)/(log(2)))
for it in range (1,itmax):
    c=(a+b)/2
    if f(a)*f(c)<0:
        b=c
    else:
        a=c
        
print('itmax: ',itmax)
print('c: ',c) #raiz
