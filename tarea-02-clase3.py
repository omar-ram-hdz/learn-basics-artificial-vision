""" 
1) Tarea: 
Usar los códigos vistos en clase para hacer la detección de un color, puede ser cualquier color, de preferencia se debe detectar
un color primario sobre un fondo blanco o un fondo que contraste con el color a detectar, solo detectar el color,
no es necesario enviar datos a la tarjeta Arduino para resolver ésta tarea, enviar el código y/o un video de evidencia.

"""

import cv2 as ocv
import numpy as np 

ID_CAMERA = 0
NAME_WINDOW_CAPTURE = "CAMARA"
NAME_WINDOW_MASK = "MASCARA"
WIDTH_CAPTURE = 642

cap = ocv.VideoCapture(ID_CAMERA)
ocv.namedWindow(NAME_WINDOW_CAPTURE)
ocv.namedWindow(NAME_WINDOW_MASK)

while True:
  ret,frame = cap.read()
  hsv = ocv.cvtColor(frame,ocv.COLOR_BGR2HSV)
  minColor = np.array([0,179,107])
  maxColor = np.array([236,255,255])
  mask = ocv.inRange(hsv,minColor,maxColor)
  contornos,_ = ocv.findContours(mask,ocv.RETR_EXTERNAL,ocv.CHAIN_APPROX_SIMPLE)
  if(len(contornos)) > 0:
    contorno_mas_grande = max(contornos,key=ocv.contourArea)
    (x,y),radio = ocv.minEnclosingCircle(contorno_mas_grande)
    x = int(x)
    y = int(y)
    centro = (x,y)
    radio = int(radio)
    if radio > 50:
      text= "COLOR DETECTADO"
      ocv.circle(frame,centro,radio,(30,255,150),4)
      ocv.putText(frame,"{},{}".format(x,y),(451, 461),ocv.FONT_ITALIC,1,(13,90,255),thickness=0)
    else:
      text = "COLOR NO DETECTADO"
      centro = (5,40)
    ocv.putText(frame,text,centro,ocv.FONT_ITALIC,1,(13,90,255),thickness=2)
    
  
  ocv.imshow(NAME_WINDOW_CAPTURE,frame)
  ocv.imshow(NAME_WINDOW_MASK,mask)
  salir = ocv.waitKey(1)
  if salir == 27:
    break

cap.release()
ocv.destroyAllWindows()