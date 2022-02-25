import numpy as np
import matplotlib.pyplot as plt
#Lazo o loop es aquel que me permite realizar acciones recurrentes sobre una lista, matriz o grupo
a=[25,7,8,10]
b=[32,3,6,7]
##Por posición
#Longitud
la=len(a)   #para determinar la longitud de una lista
#Rango
ra=range(la)
# a=[25,7, 8,10]
#     0 1  2  3    El rango que me sale indica que la numeracion empieza en 0 y tengo 4 elementos

for i in ra:
    fa=a[i]+np.pi - np.sin(np.pi/4)
    print(fa)

ga=np.zeros(la)  # genero una lista de ceros con longitud de a
for i in ra:
    fa=a[i]+np.pi - np.sin(np.pi/4)
    ga[i]=fa

print(ga)
plt.plot(ga,a)
plt.show()