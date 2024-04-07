# Hacer anotaciones
import cv2 as ocv
RUTA_IMAGEN = "./img/mano.png"
IMAGEN = ocv.imread(RUTA_IMAGEN)

# 342,288/660,375
#(imagen,(origenX,origenY),(finalX,finalY),(B,G,R))
linea= ocv.line(
  IMAGEN,
  (342,288),
  (660,375),
  (0,255,0), 
  thickness=10, 
  lineType=ocv.LINE_AA
)

# (img, centro(x,y), radio, color, grosorLinea, tipo linea )
# 520,360
circulo = ocv.circle(
  IMAGEN, 
  (520,360),
  80,
  (0,0,255),
  thickness=10, 
  lineType=ocv.LINE_AA
)

# (img, (origenX,origenY), puntoF(x,y), color, ancho, tipo)
rectangulo = ocv.rectangle(
  IMAGEN, 
  (255,118), 
  (888,495),
  (255,0,0),
  thickness=10,
  lineType=ocv.LINE_AA
)

# (img,texto, origen(x,y),tipoLetra, tamanio, color, grosor, tipo)
text = ocv.putText(
  IMAGEN, 
  "Mano detectada", 
  (300,90),
  ocv.FONT_ITALIC,
  1,
  (223, 180, 82),
  thickness=2,
  lineType=ocv.LINE_AA
)

ocv.imshow("ANOTACIONES", IMAGEN)
ocv.waitKey(0)