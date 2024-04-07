# Rotar una imagen
import cv2 as ocv
RUTA_IMAGEN = "./img/logo-asociacion.jpg"
imagen = ocv.imread(RUTA_IMAGEN)
voltear1= ocv.flip(imagen,-1)
rotar = ocv.rotate(imagen,ocv.ROTATE_90_COUNTERCLOCKWISE)

ocv.imshow("IMAGEN ORIGINAL",imagen)
ocv.imshow("IMAGEN VOLTEADA",voltear1)
ocv.imshow("IMAGEN ROTATE",voltear1)

ocv.waitKey(0)