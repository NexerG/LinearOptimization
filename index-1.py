import matplotlib.pyplot as plt
import numpy as np
import math
from Algoritmai.Dalinimas import Dvis
from Algoritmai.Golden import Gvis
from Algoritmai.Newtons import Nvis

#konstantos
a=0
b=10
GR=(math.sqrt(5)-1)/2

#funkcija
x = np.linspace(0, 10, 200)
y = (np.power((np.power(x,2)-6), 2)/6)-1

#isvestine y
dy=(2*x*(np.power(x,2)-6))/3

#vizualizacijos
###Golden Ratio
Gx=Gvis(a,b,GR)
Gy=(np.power((np.power(Gx,2)-6), 2)/6)-1

###Dalinimas
Dx=Dvis(0,10)
Dy=(np.power((np.power(Dx,2)-6), 2)/6)-1

###Niutonas
Nx=Nvis(5)
Ny=(np.power((np.power(Nx,2)-6), 2)/6)-1

#plot
fig, (axG,axD,axN) = plt.subplots(3)
#sudarom Golden ratio plota
axG.plot(x, y, 'k')
axG.plot(Gx,Gy,'mo')
axG.set_xlabel("X")
axG.set_ylabel("Y(x) Golden")

#sudarom Dalinimo plota
axD.plot(x, y, 'k')
axD.plot(Dx,Dy,'mo')
axD.set_xlabel("X")
axD.set_ylabel("Y(x) Dalinimas")

#sudarom Niutono plota
axN.plot(x, y, 'k')
axN.plot(Nx,Ny,'mo')
axN.set_xlabel("X")
axN.set_ylabel("Y(x) Newtons")

plt.show()