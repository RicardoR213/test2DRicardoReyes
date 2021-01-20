#Ricardo Reyes Benigno
import matplotlib.pyplot as plt
import numpy as np
import math as mt

plt.axis([-20,130,-20,130])
plt.axis('on')
plt.grid(True)
plt.title('Test 2D')
plt.xlabel("Eje x")
plt.ylabel("Eje y")
#Radio
r=25
#Centro del círculo
xc=40
yc=60

#Plotear el círculo
alpha1=mt.radians(1)

alpha2=mt.radians(360)

dalpha=mt.radians(1)

plt.scatter(xc,yc,s=1,color='blue')

print (np.arange(alpha1,alpha2,dalpha))

for alpha in np.arange(alpha1,alpha2,dalpha):

    x=xc+r*mt.sin(alpha)

    y=yc+r*mt.cos(alpha)

    plt.scatter(x,y,s=1,color=(5/10,8/10,5/10))


#Se crea el rectángulo
xp1=80
xp2=80
xp3=0
xp4=0
yp1=0
yp2=-60
yp3=-60
yp4=0
#Plotear las líneas del rectángulo
xg1=xc+xp1 #Coordenadas en Xg, Yg -->Sistema global
yg1=yc+yp1
xg2=xc+xp2 #Coordenadas en Xg, Yg -->Sistema global
yg2=yc+yp2
xg3=xc+xp3 #Coordenadas en Xg, Yg -->Sistema global
yg3=yc+yp3
xg4=xc+xp4 #Coordenadas en Xg, Yg -->Sistema global
yg4=yc+yp4

#Se inicia la traslacion del rectángulo
xg=np.array([xg1,xg2,xg3,xg4,xg1])
yg=np.array([yg1,yg2,yg3,yg4,yg1])
plt.plot(xg,yg,color=(5/10,8/10,5/10))

dx=-40
dy=30
xg+=dx
yg+=30
plt.plot(xg,yg,color=(5/10,8/10,5/10))

plt.show()