import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt


rgbHEBM=cv2.imread('v3.jpg')
plt.figure(0)
plt.imshow(rgbHEBM)
C1 = rgbHEBM[:,:,0]
C2 = rgbHEBM[:,:,1]
C3 = rgbHEBM[:,:,2]

a= C1.shape[0]
b= C1.shape[1]
n_i=np.zeros((256))
y=np.zeros((a,b))

n_i2=np.zeros((256))
y2=np.zeros((a,b))

n_i3=np.zeros((256))
y3=np.zeros((a,b))

for i in range(a):
    for j in range(b):
        pxl=C1[i,j]#Valor del pixel en la posicion (i,j)
        pxl2=C2[i,j]
        pxl3=C3[i,j]
        n_i[pxl]+=1
        n_i2[pxl2]+=1
        n_i3[pxl3]+=1
pro=n_i/(a*b)
ecualiza=np.zeros(256)
acumulado = 0
pro2=n_i2/(a*b)
ecualiza2=np.zeros(256)
acumulado2 = 0
pro3=n_i3/(a*b)
ecualiza3=np.zeros(256)
acumulado3 = 0

for k in range(256):
        acumulado = pro[k] + acumulado
        ecualiza[k]=acumulado 
        
        acumulado2 = pro2[k] + acumulado2
        ecualiza2[k]=acumulado2
        
        cumulado3 = pro3[k] + acumulado3
        ecualiza3[k]=acumulado3
#Treshold
G=input("Ingrese un valor entre 0 y 255: ")
G=int(G)
#G=int(request.form.get("G"))
#####
c_i=np.zeros((256))
c_i2=np.zeros((256))
c_i3=np.zeros((256))
for i in range(a):
    for j in range(b):
        pxl=C1[i,j]#Valor del pixel en la posicion (i,j)
        pxl2=C2[i,j]#Valor del pixel en la posicion (i,j)
        pxl3=C3[i,j]#Valor del pixel en la posicion (i,j)
        if pxl<=G:
            c_i[pxl]+=1
        if pxl2<=G:
            c_i2[pxl2]+=1
        if pxl3<=G:
            c_i3[pxl3]+=1
for i in range(256):
    if c_i[i]>0:
        c_i[i]=1/c_i[i]
    if c_i2[i]>0:
        c_i2[i]=1/c_i2[i]
    if c_i3[i]>0:
        c_i3[i]=1/c_i3[i]
L_k=np.zeros(256)
acumulado = 0
L_k2=np.zeros(256)
acumulado2 = 0
L_k3=np.zeros(256)
acumulado3 = 0
for k in range(256):
        acumulado = c_i[k] + acumulado
        L_k[k]=acumulado 
        acumulado2 = c_i2[k] + acumulado2
        L_k2[k]=acumulado2 
        acumulado3 = c_i3[k] + acumulado3
        L_k3[k]=acumulado3
N_c=sum(c_i)
G_g=255/N_c
L_k=L_k*G_g

N_c2=sum(c_i2)
G_g2=255/N_c2
L_k2=L_k2*G_g2

N_c3=sum(c_i3)
G_g3=255/N_c3
L_k3=L_k3*G_g3
for i in range(a):
    for j in range(b):
       entrada =C1[i,j]
       y[i,j]=L_k[entrada]
       entrada2 =C2[i,j]
       y2[i,j]=L_k2[entrada2]
       entrada3 =C3[i,j]
       y3[i,j]=L_k3[entrada3]
       
plt.figure(1)
plt.imshow
       
plt.figure(2)
plt.imshow(y2)

plt.figure(3)
plt.imshow(y3)

rgbArray = np.zeros((a,b,3), 'uint8')
rgbArray[..., 0] = y
rgbArray[..., 1] = y2
rgbArray[..., 2] = y3
salidaHEBM = Image.fromarray(rgbArray)
plt.figure(4)
plt.imshow(salidaHEBM)