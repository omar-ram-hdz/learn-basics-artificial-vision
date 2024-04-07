
import mediapipe as mp  # pip install mediapipe
import cv2

# sirve para dibujar con las utilidades de mediapipe
mp_dibujo = mp.solutions.drawing_utils

# para inicializar la solucion de detección de manos
mp_manos = mp.solutions.hands

objeto_hands = mp_manos.Hands(static_image_mode = False,
                              max_num_hands = 2,
                              min_detection_confidence = 0.5)


cap = cv2.VideoCapture(2)

ventana1 = "Detección de manos"
cv2.namedWindow(ventana1, cv2.WINDOW_NORMAL)
cv2.resizeWindow(ventana1, 720, 420)


while True:
    ret, frame =  cap.read()

    RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    resultados = objeto_hands.process(RGBframe)

    if resultados.multi_hand_landmarks:
        for puntos in resultados.multi_hand_landmarks:

            mp_dibujo.draw_landmarks(frame, puntos, mp_manos.HAND_CONNECTIONS)


    cv2.imshow(ventana1, frame)

    salir = cv2.waitKey(1)
    if salir == 27:
        break

cap.release()
cv2.destroyAllWindows()



