#Metodo de la iteracion funcional

from pylab import *
from scipy import *
from math  import ceil #ceil es el techo superior y floor el inferior


#Definir una función; la que me digan

def f(x):
    if problema==1:
        f=x+sin(x)-x**3
    elif problema==2:
        f=exp(x)-13*x**2
    return f

#problema = numero para ir mas rapido
problema=eval(input('dame el problema    '))

tolabs=1.e-5
tolrel=1.e-5
itmax=30000

x=1  #aproximacion al cero del metodo de biseccion
c=0.1
#Si no converge cambia el signo con c pequeño
#Operar con c pequeño proximo a 0

for it in range (1,itmax):
    y=x+c*f(x)
    dif=abs(y-x)
    if dif<=max(tolabs,tolrel*abs(y)):
        print('Convergencia')
        break
    x=y
        
print('it: ',it)
print('f(x): ',f(x))
print('dif: ',dif)
print('x: ',x)
