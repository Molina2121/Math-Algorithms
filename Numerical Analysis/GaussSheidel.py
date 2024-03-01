from pylab import *
from scipy import linalg

nombre='sist1.txt'

myfile=open(nombre)

n=int(myfile.readline())

a=zeros((n+1,n), float64)
b=zeros(n, float64)
x=zeros(n, float64)
y=zeros(n, float64)

a=loadtxt(nombre,skiprows=1) 
#Lee el fichero y coge los números y los almacena en a
#skiprows, sirve para saltar la fila que no necesitamos leer, por ejemplo en estecas
#no necesitamos leer la fila uno porque contiene la dimensión

b=a[n]

a=delete(a,n,axis=0) #borra de la matriz a la fila n, axis=0 conserva la matriz

myfile.close

print('\n Matriz: ','\n',a,'\n')
print('\n','Vector: ','\n',b,'\n')

itermax=300
eps=1.e-10
toldiv=1.e+3
tol=1.e-8

fin='nofin'
for  i in range(0,n):
    if (abs(a[i,i])<=eps):
        print ('elemento diagonal nulo')
        fin='nulo'
        sys.exit()
x[0:n]=1.0e+0

for k in range(itermax):
    for i in range(0,n):
        y[i]=(b[i]-dot(a[i,0:i],y[0:i])-dot(a[i,i+1:n],x[i+1:n]))/a[i,i]
    dif=norm(x-y,2)
    if(dif<=tol):
        print ('convergencia alcanzada en la iteración',k+1)
        print ('la solucion es:')
        print (y)
        print ('error: ',dif)
        fin='conv'
        break
    if(dif>=toldiv):
        print ('el metodo diverge en la iteracion',k)
        fin='div'
        break
    x=copy(y)
if fin=='nofin':
        print ('no se ha alcanzado la convergencia tras', itermax, 'iteraciones')
        print ('la aproximacion a la solucion es: ', y)
        print ('error: ',dif)
        
              