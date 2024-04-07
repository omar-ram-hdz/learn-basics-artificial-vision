import mediapipe as mp  # pip install mediapipe
import cv2
import serial

# sirve para dibujar con las utilidades de mediapipe
mp_dibujo = mp.solutions.drawing_utils

# para inicializar la solución de detección de manos
mp_manos = mp.solutions.hands

objeto_hands = mp_manos.Hands(
    static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5
)


cap = cv2.VideoCapture(0)

ventana1 = "Detección de manos"
cv2.namedWindow(ventana1, cv2.WINDOW_NORMAL)
cv2.resizeWindow(ventana1, 720, 420)

try:
    puerto = serial.Serial("COM3", 9600, timeout=1)
except:
    print("No hubo conexión")

dedoPlg = 0
dedoInd = 0
dedoMed = 0
dedoAnl = 0
dedoMnq = 0
dedos_detectados = 0


while True:
    ret, frame = cap.read()
    # frame = cv2.flip(frame, 1)

    RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    resultados = objeto_hands.process(RGBframe)

    if resultados.multi_hand_landmarks:
        for puntos in resultados.multi_hand_landmarks:

            # mp_dibujo.draw_landmarks(frame, puntos, mp_manos.HAND_CONNECTIONS)

            dedo_pulgar = puntos.landmark[4]
            dedo_indice = puntos.landmark[8]
            dedo_medio = puntos.landmark[12]
            dedo_anular = puntos.landmark[16]
            dedo_menique = puntos.landmark[20]
            punto_central = puntos.landmark[5]

            alto, ancho, canales = frame.shape

            coorPlgX, coorPlgY = int(dedo_pulgar.x * ancho), int(dedo_pulgar.y * alto)
            coorIndX, coorIndY = int(dedo_indice.x * ancho), int(dedo_indice.y * alto)
            coorMedX, coorMedY = int(dedo_medio.x * ancho), int(dedo_medio.y * alto)
            coorAnlX, coorAnlY = int(dedo_anular.x * ancho), int(dedo_anular.y * alto)
            coorMnqX, coorMnqY = int(dedo_menique.x * ancho), int(dedo_menique.y * alto)

            coorCenX, coorCenY = int(punto_central.x * ancho), int(
                punto_central.y * alto
            )

            cv2.circle(frame, (coorPlgX, coorPlgY), 20, (0, 255, 0), thickness=-1)
            cv2.circle(frame, (coorIndX, coorIndY), 20, (0, 255, 0), thickness=-1)
            cv2.circle(frame, (coorMedX, coorMedY), 20, (0, 255, 0), thickness=-1)
            cv2.circle(frame, (coorAnlX, coorAnlY), 20, (0, 255, 0), thickness=-1)
            cv2.circle(frame, (coorMnqX, coorMnqY), 20, (0, 255, 0), thickness=-1)
            cv2.circle(frame, (coorCenX, coorCenY), 20, (0, 0, 255), thickness=-1)
            # dedo pulgar
            if coorPlgX < coorCenX:
                dedoPlg = 1
            else:
                dedoPlg = 0

            # medio indice
            if coorIndY < coorCenY:
                dedoInd = 1
            else:
                dedoInd = 0

            # dedo medio
            if coorMedY < coorCenY:
                dedoMed = 1
            else:
                dedoMed = 0

            # dedo anular
            if coorAnlY < coorCenY:
                dedoAnl = 1
            else:
                dedoAnl = 0

            # dedo menique
            if coorMnqY < coorCenY:
                dedoMnq = 1
            else:
                dedoMnq = 0

            dedos_detectados = dedoPlg + dedoInd + dedoMed + dedoAnl + dedoMnq
            try:
                puerto.write(
                    f"{dedoPlg}A{dedoInd}B{dedoMed}C{dedoAnl}D{dedoMnq}\n".encode()
                )
            except:
                print("No se pueden enviar los datos")

        print(dedos_detectados)
        cv2.putText(
            frame,
            f"Num dedos: {dedos_detectados}",
            (100, 100),
            cv2.FONT_ITALIC,
            2,
            (0, 0, 255),
            thickness=5,
        )

    else:
        cv2.putText(
            frame,
            "No hay manos",
            (100, 100),
            cv2.FONT_ITALIC,
            2,
            (0, 0, 255),
            thickness=5,
        )
        dedos_detectados = 0

    cv2.imshow(ventana1, frame)

    salir = cv2.waitKey(1)
    if salir == 27:
        break

cap.release()
cv2.destroyAllWindows()

