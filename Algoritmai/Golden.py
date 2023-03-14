import numpy as np

dist=0
xs=[]
over=[]
under=[]

def Gvis(a,b,GR):
    #for i in range(10):
    dist=D(GR,a,b)
    iter=0
    while dist>10**(-4):
        dist=D(GR,a,b)
        x1=a+dist
        x2=b-dist
        y1=(np.power((np.power(x1,2)-6),2)/6)-1
        y2=(np.power((np.power(x2,2)-6),2)/6)-1
        if(y1>y2):
            over.append(x1)
            under.append(x2)
            b=x1
        else:
            over.append(x2)
            under.append(x1)
            a=x2
        print(iter,end='')
        print(" Golden iteracija: atstumas=",end='')
        print(format(dist,".4f"))
        iter=iter+1

    print("Auksinis pjuvis: ", end='')
    print(iter,end='')
    print(" iteracijos")
    print("---------------")
    xs.append(under)
    xs.append(over)
    return xs

#additional fjos
def D(GR,a,b):
    return GR*(b-a)

