from pylab import *
from scipy import linalg

nombre='ex1.txt'

myfile=open(nombre)

n=int(myfile.readline())

a=zeros((n+1,n), float64)
x=zeros(n, float64)
y=zeros(n, float64)


x[0]=1 #escribir aqui el vector que me den
x[1]=0
x[2]=0
#for i in range (0,n):
#    x[i]=1
#for i in range (2,n):
   # x[i]=0        -> añado este for para el ejemplo 7 porque el vector 1,1,1,... está muy cerca de x
   #CAMBIAR LA N DEL ANTERIOR FOR POR 2

a=loadtxt(nombre,skiprows=1) 
#Lee el fichero y coge los números y los almacena en a
#skiprows, sirve para saltar la fila que no necesitamos leer, por ejemplo en estecas
#no necesitamos leer la fila uno porque contiene la dimensión

a=delete(a,n,axis=0) #borra de la matriz a la fila n, axis=0 conserva la matriz

myfile.close

itmax=60000
tol=1.e-7
lo=2


lu,piv=linalg.lu_factor(a-lo*eye(n)) #eye(n) identidad de dimensión n
x=1/norm(x,2)*x  #normalizacion inicial
for it in range (1,itmax):
    y=linalg.lu_solve((lu,piv),x)
    dif=min(norm((y/norm(y,2))-x,2),norm(y/norm(y,2)+x,2))
    x=1/norm(y,2)*y
    if (dif<= tol*norm(y,2)):
        print ('Convergencia')
        break

l=dot(x,dot(a,x))

    
print ('iteraciones: ',it)
print ('lambda: ',l)
print ('vector x: ',x)
print ('dif: ',dif)