# Recortar imágenes y videos
import cv2 as ocv
IMAGEN = "./img/logo-asociacion.jpg"

imagen = ocv.imread(IMAGEN)
recorte = imagen[0:255,0:255]
ocv.imshow("Imagen Original",imagen)
ocv.imshow("Imagen Recortada",recorte)

ocv.waitKey(0)