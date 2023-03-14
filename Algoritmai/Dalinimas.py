import numpy as np

def Dvis(st,en):
    iter=0
    xs=[0,10]
    while en-st>10**(-4):
        xmid=(np.power((np.power(st+(en-st)/2,2)-6), 2)/6)-1
        xen=(np.power((np.power(en,2)-6), 2)/6)-1
        xst=(np.power((np.power(st,2)-6), 2)/6)-1
        if xmid<xen:
            xs.append(st+(en-st)/2)
            en=st+(en-st)/2
        elif xmid<xst: 
            xs.append(st+(en-st)/2)
            st=st+(en-st)/2
        print(iter,end='')
        print(" Dalinimo iteracija: atstumas=",end='')
        print(format(en-st,".4f"),end='')
        print("  ribos:[",end='')
        print(format(st,".4f"),end='')
        print(" ; ",end='')
        print(format(en,".4f"),end='')
        print("]")
        iter=iter+1
    print("Dalinimo metodas: ", end='')
    print(iter,end='')
    print(" iteracijos")
    print("---------------")
    return xs
    