# Captura de video
import cv2 as ocv

captura = ocv.VideoCapture(0)

ocv.namedWindow("CAMARA") 
# ocv.resizeWindow("CAMARA", 720,480)

while True:
  ret, frame = captura.read()
  if(ret):
    ocv.imshow("CAMARA",frame)
  salir = ocv.waitKey(1)
  if salir == 27:
    break

captura.release()
ocv.destroyAllWindows()