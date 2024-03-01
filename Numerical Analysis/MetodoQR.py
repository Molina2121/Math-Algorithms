from pylab import *
from scipy import linalg

nombre='ex1.txt'

myfile=open(nombre)

n=int(myfile.readline())

a=zeros((n+1,n), float64)
i=1
j=1

a=loadtxt(nombre,skiprows=1) 
a=delete(a,n,axis=0) 
myfile.close

itmax=60000
tol=1.e-3

for it in range (1,itmax):
    Q,R=qr(a)
    a=dot(R,Q)
    dif=abs(a[1,0])
    for i in range (1,n):
        for j in range (0,i):
            if (dif<abs(a[i,j])):
                dif=abs(a[i,j])
    if (dif<=tol):
        print ('Convergencia')
        break

print('iteraciones: ',it)
for i in range (0,n):
    print('aii: ', a[i,i])
print('dif: ', dif)

print('\n',eigvals(a))