import cv2
import mediapipe as mp

# Inicializar el módulo de detección de manos de Mediapipe
mp_dibujo = mp.solutions.drawing_utils
mp_manos = mp.solutions.hands

# Asignar el modelo a la variable hands
objeto_hands = mp_manos.Hands(
    static_image_mode=False, max_num_hands=2, min_detection_confidence=0.1
)

# Inicializar la cámara
cap = cv2.VideoCapture(0)

ventana1 = "captura"
cv2.namedWindow(ventana1, cv2.WINDOW_NORMAL)
cv2.resizeWindow(ventana1, 720, 420)

while True:
    ret, frame = cap.read()  # Capturar un fotograma

    # Convertir a formato RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Obtener resultados de la detección de manos
    resultados = objeto_hands.process(rgb_frame)

    # Verificar si se detectaron manos
    if resultados.multi_hand_landmarks:
        for puntos in resultados.multi_hand_landmarks:

            # Dibujar líneas que conectan los landmarks
            mp_dibujo.draw_landmarks(frame, puntos, mp_manos.HAND_CONNECTIONS)

    # Mostrar el fotograma
    cv2.imshow(ventana1, frame)

    # Salir del bucle si se presiona la tecla 'q'
    salir = cv2.waitKey(1)
    if salir == 27:
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
