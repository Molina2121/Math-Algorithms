from pylab import *
from scipy import *
from math import *



#Definir una función
#Escribir la funcion que nos den... si es sistema recuerda 
#x[0] = x; x[1] = y ... 

def f(x):
    if problema==1:
        f=[x[0]**2-3]
    elif problema==2:
        f=[exp(x[0])-13*x[0]**2]
    elif problema==3:
        f=[(x[0]**2-x[1]**2)/2-x[0]+7/24,x[0]*x[1]-x[1]+1/9]
    elif problema==4:
        f=[x[0]**3+x[0]*x[1]**2-2,x[0]**2*x[1]+x[1]**3-1]
    elif problema==5:
        f=[4*(x[0]-3)**2+3*(x[1]-1)**2-96,log(x[1]-2)-1-cos(x[0]/2+2)]
        
        
    elif problema==6:
        
        f=[4*((x[0]-3)**2)+3*((x[1]-1)**2)-96,-log(x[1]-2)+1+cos(x[0]/2+2)]
        
    return f
#derivada de f... si es sistema jacobiano; primero derivada 
#de la primera ecuacion en funcion de x,y luego de la segunda

def df(x):
    if problema==1:
            df=[[2*x[0]]]
    elif problema==2:
            df=[[exp(x[0])-26*x[0]]]
    elif problema==3:
            df=[[x[0]-1,-x[1]],[x[1],x[0]-1]]
    elif problema==4:
            df=[[3*x[0]**2+x[1]**2,2*x[0]*x[1]],[2*x[0]*x[1],x[0]**2+3*x[1]**2]]
    elif problema==5:
            df=[[-8*(x[0]-3),-6*(x[1]-1)],[-sin((x[0]/2)+2)/2,-1/(x[1]-2)]]
    elif problema==6:
            df=[[-8*(x[0]-3),-6*(x[1]-1)],[-sin((x[0]/2)+2)/2,-1/(x[1]-2)]]
    return df

#problema = numero para ir mas rapido :)
problema=5

if problema==1:
    x=[0.5]
elif problema==2:
    x=[0.0]
elif problema==3:
    x=[0.0,0.0]
elif problema==4:
    x=[0.0,0.5]
elif problema==5:
    x=[0.0,0.5,0.2]
elif problema==6:
    x=[0,4]

tolabs=1.e-8
tolrel=1.e-8
itmax=30000

print(f([0,4]))

for it in range (1,itmax):
    print(x)
    print(f(x))
    dx=solve(df(x),f(x))
    y=x-dx
    dif=norm(dx,2)
    if dif<=max(tolabs,tolrel*norm(y,2)):
        print('Convergencia')
        break
    x=y

print('f(x): ',f(x)) #valor de la raiz en f(X)
print('it: ',it)
print('dif: ',dif)
print('x: ',x) #raiz




