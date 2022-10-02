
import matplotlib.pyplot as plt
import numpy as np
import cv2

def un (filename):
    
    rgbUnsharp=cv2.imread(filename)  
    plt.figure(0)
    plt.imshow(rgbUnsharp)
    kernel = np.array([
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
        ])
    imagen=rgbUnsharp
    salidaUnsharp=cv2.filter2D(rgbUnsharp, -1, kernel)
    cv2.imwrite ('un.jpg', salidaUnsharp)