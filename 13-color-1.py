import cv2 as ocv
import numpy as np
from os import system
import serial

ID_CAMERA = 0
NAME_WINDOW_CAPTURE = "CAPTURA"
NAME_WINDOW_MASK = "MASCARA"
WIDTH_CAPTURE = 642

cap = ocv.VideoCapture(ID_CAMERA)
ocv.namedWindow(NAME_WINDOW_CAPTURE )
ocv.namedWindow(  NAME_WINDOW_MASK, ocv.WINDOW_NORMAL)
puerto = serial.Serial("COM3", 9600, timeout=1)



while True:
  ret,frame = cap.read()
  hsv = ocv.cvtColor(frame,ocv.COLOR_BGR2HSV)
  minColor = np.array([0,179,107])
  maxColor = np.array([236,255,255])
  mask = ocv.inRange(hsv, minColor, maxColor)
  contornos, _ = ocv.findContours(mask,ocv.RETR_EXTERNAL,ocv.CHAIN_APPROX_SIMPLE)
  if len(contornos) > 0:
    contorno_mas_grande = max(contornos,key=ocv.contourArea)
    (x,y),radio = ocv.minEnclosingCircle(contorno_mas_grande)
    # percent = (int(x)/WIDTH_CAPTURE)
    # ard = percent*255
    x = int(x)
    y = int(y)
    centro = (x,y)
    radio = int(radio)
    if radio > 50:
      text = "COLOR DETECTADO"
      ocv.circle(frame,centro,radio,(30,255,150),5)
      
    else: 
      text = "COLOR NO DETECTADO"
      centro = (5,40)
    ocv.putText(frame,text,centro, ocv.FONT_ITALIC, 1, (13,90,255),thickness=2)
    system('cls')
    puerto.write(f"{x}A{y}".encode())
    # print("{}%".format(percent*100))
    # print(ard)
    
  # ocv.drawContours(frame,contornos, -1, (255,255,120),5)
  ocv.imshow(NAME_WINDOW_CAPTURE, frame)
  ocv.imshow(NAME_WINDOW_MASK, mask)
  salir = ocv.waitKey(1)
  if salir == 27:
    break

cap.release()
ocv.destroyAllWindows()