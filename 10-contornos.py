import cv2 as ocv
RUTA_IMAGEN = "./img/logo-asociacion.jpg"
IMAGEN = ocv.imread(RUTA_IMAGEN)

imagenBN = ocv.cvtColor(IMAGEN,ocv.COLOR_BGR2GRAY)

# Aplicar umbral
umbral, img_binary = ocv.threshold(imagenBN, 128,255,ocv.THRESH_BINARY_INV)

# (imagen, modo, metodo, contorno , offset)
contornos, jerarquia = ocv.findContours(img_binary, ocv.RETR_LIST, ocv.CHAIN_APPROX_SIMPLE)

# Dibujar contorno (contornor, indice de contornos, color,tamaño)
ocv.drawContours(IMAGEN,contornos,-1,(80,200,34),3)

ocv.imshow("IMAGEN ORIGINAL",IMAGEN)
ocv.imshow("IMAGEN BINARY",img_binary)

ocv.waitKey(0)
