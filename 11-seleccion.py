import cv2
import numpy as np

# Inicializar la cámara
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture(r"C:\Users\robot\Documents\RGBvideo.mp4")

ventana = "captura"
cv2.namedWindow(ventana, cv2.WINDOW_NORMAL)
cv2.resizeWindow(ventana, 720, 720)

# Función de retroalimentación para barras deslizantes
def barras(valor):
        # Obtener los valores actuales de las barras deslizantes
    lower_hue = cv2.getTrackbarPos('Hue min', ventana)
    lower_saturation = cv2.getTrackbarPos('Saturation min', ventana)
    lower_value = cv2.getTrackbarPos('Value min', ventana)

    upper_hue = cv2.getTrackbarPos('Hue max', ventana)
    upper_saturation = cv2.getTrackbarPos('Saturation max', ventana)
    upper_value = cv2.getTrackbarPos('Value max', ventana)

    # Imprimir los valores
    print(f'Inferior: [{lower_hue}, {lower_saturation}, {lower_value}]')
    print(f'Superior: [{upper_hue}, {upper_saturation}, {upper_value}]')


# Crear barras deslizantes para ajustar valores de color
cv2.createTrackbar('Hue min', ventana, 0, 255, barras)
cv2.createTrackbar('Saturation min', ventana, 0, 255, barras)
cv2.createTrackbar('Value min', ventana, 0, 255, barras)

cv2.createTrackbar('Hue max', ventana, 0, 255, barras)
cv2.createTrackbar('Saturation max', ventana, 0, 255, barras)
cv2.createTrackbar('Value max', ventana, 0, 255, barras)

while True:
    # Capturar un fotograma
    ret, frame = cap.read()

    # Convertir el fotograma a formato HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Obtener los valores actuales de las barras deslizantes
    lower_hue = cv2.getTrackbarPos('Hue min', ventana)
    lower_saturation = cv2.getTrackbarPos('Saturation min', ventana)
    lower_value = cv2.getTrackbarPos('Value min', ventana)

    upper_hue = cv2.getTrackbarPos('Hue max', ventana)
    upper_saturation = cv2.getTrackbarPos('Saturation max', ventana)
    upper_value = cv2.getTrackbarPos('Value max', ventana)

    # Definir el rango de colores en formato HSV
    lower_blue = np.array([lower_hue, lower_saturation, lower_value])
    upper_blue = np.array([upper_hue, upper_saturation, upper_value])

    # Aplicar la máscara para detectar los colores azules
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Mostrar la máscara
    cv2.imshow(ventana, mask)

    # Salir del bucle si se presiona la tecla 'q'
    t = cv2.waitKey(1)
    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()
