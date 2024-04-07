import cv2 as ocv
import numpy as np

CAP = ocv.VideoCapture(0)
VENTANA = "CAPTURA DE VIDEO"

ocv.namedWindow(VENTANA, ocv.WINDOW_NORMAL)

while True:
  ret, frame = CAP.read()
  hsv = ocv.cvtColor(frame,ocv.COLOR_BGR2HSV)
  
  # Rango de color
  minColor = np.array([13,54,146])
  maxColor = np.array([85,232,253])
  
  # (imgHSV, minColor, maxColor)
  mask = ocv.inRange(hsv,minColor,maxColor)
  
  ocv.imshow(VENTANA,mask)
  salir = ocv.waitKey(1)
  if salir == 27:
    break


CAP.release()
ocv.destroyAllWindows()