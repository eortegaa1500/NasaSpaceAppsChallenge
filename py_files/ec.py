import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def ec(filename):  
    rgb=cv2.imread(filename)
    plt.figure(0)
    plt.imshow(rgb)
    C1 = rgb[:,:,0]
    C2 = rgb[:,:,1]
    C3 = rgb[:,:,2]
    histo=np.zeros(256)
    histo2=np.zeros(256)
    histo3=np.zeros(256)
    filas=C1.shape[0] #
    columnas=C1.shape[1]
    filas2=C2.shape[0] #
    columnas2=C2.shape[1]
    filas3=C3.shape[0] #
    columnas3=C3.shape[1]
    salida1=np.zeros((filas,columnas))
    salida2=np.zeros((filas2,columnas2))
    salida3=np.zeros((filas3,columnas3))
    
    for i in range(filas):
        for j in range(columnas):
            pixel = int(C1[i,j])
            pixel2 = int(C2[i,j])
            pixel3 = int(C3[i,j])
            histo[pixel]  +=1   #ocurrencia en el univero
            histo2[pixel2]  +=1   #ocurrencia en el univero
            histo3[pixel3]  +=1 
    pro = histo/(filas*columnas)  
    pro2 = histo2/(filas2*columnas2)
    pro3 = histo3/(filas3*columnas3)
    ecualiza=np.zeros(256)
    ecualiza2=np.zeros(256)
    ecualiza3=np.zeros(256)
    acumulado = 0
    acumulado2 = 0
    acumulado3 = 0
    for k in range(256):
        acumulado = pro[k] + acumulado
        acumulado2 = pro2[k] + acumulado2
        acumulado3 = pro3[k] + acumulado3
        ecualiza[k]=acumulado * 255.0  
        ecualiza2[k]=acumulado2 * 255.0   
        ecualiza3[k]=acumulado3 * 255.0            
    for i in range(filas):
        for j in range(columnas):
            entrada = int(C1[i,j])
            entrada2 = int(C2[i,j])
            entrada3 = int(C3[i,j])
            salida1[i,j]=ecualiza[entrada]
            salida2[i,j]=ecualiza2[entrada2]
            salida3[i,j]=ecualiza3[entrada3]
    rgbArray = np.zeros((filas,columnas,3), 'uint8')
    rgbArray[..., 0] = salida1
    rgbArray[..., 1] = salida2
    rgbArray[..., 2] = salida3
    salida = Image.fromarray(rgbArray)
    #plt.imshow(salida)
    #salida1.save('salida1.jpg')
    #salida2.save('salida2.jpg')
    #salida3.save('salida3.jpg')
    salida.save('ec.jpg')
    
