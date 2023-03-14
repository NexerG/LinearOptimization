import numpy as np

def Nvis(x):
    iter=0
    i=1
    xs=[]
    while i>10**(-4):
        xs.append(x)
        i = ((np.power((np.power(x,2)-6), 2)/6)-1)/((2*x*(np.power(x,2)-6))/3)
        x=x-i
        print(iter,end='')
        print(" Niutono iteracija: atstumas = ",end='')
        print(format(i,".4f"),end='')
        print("  X = ",end='')
        print(format(x,".4f"))
        iter=iter+1
    print("Niutono metodas: ", end='')
    print(iter,end='')
    print(" iteracijos")
    return xs