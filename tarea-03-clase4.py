""" 
1) Tarea: 
Escribe un programa en Python que sea capaz de detectar dos gestos de la mano con el video de una cámara web o una cámara virtual como Droidcam, como lo hicimos en clase, los gestos a detectar son el de pulgar arriba y el gesto de poner la mano extendida frente a la cámara.

Gesto de Pulgar Arriba: Se debe detectar cuando el pulgar esté levantado hacia arriba, y mostrar en pantalla un mensaje que diga "Pulgar arriba".

Gesto de Mano Extendida: Se debe detectar cuando todos los dedos estén extendidos, y mostrar en pantalla un mensaje que diga "Mano extendida"
"""

import mediapipe as mp
import cv2 as ocv

WINDOW_NAME = "RECOGNITION"
CAMERA_ID = 0


# def calcCoords(finger):
#     global WINDOW_ALTO, WINDOW_ANCHO
#     return int(finger.x * WINDOW_ANCHO, finger.y * WINDOW_ALTO)


def calcCoordsY(finger):
    global WINDOW_ALTO
    return int(finger.y * WINDOW_ALTO)


def calcCoordsX(finger):
    global WINDOW_ANCHO
    return int(finger.x * WINDOW_ANCHO)


mp_dibujo = mp.solutions.drawing_utils
mp_manos = mp.solutions.hands

objeto_hands = mp_manos.Hands(
    static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5
)

cap = ocv.VideoCapture(CAMERA_ID)
ocv.namedWindow(WINDOW_NAME)

FINGERS = ["Pulgar", "Indice", "Medio", "Anular", "Menique"]
fingers = {
    "pulgar": 0,
    "indice": 0,
    "medio": 0,
    "anular": 0,
    "menique": 0,
}
punto_central = {"cords": 0, "calc": 0}
UP_FINGERS = []
FINAL_TEXT = ""

while True:
    ret, frame = cap.read()
    RGBFrame = ocv.cvtColor(frame, ocv.COLOR_BGR2RGB)
    res = objeto_hands.process(RGBFrame)
    WINDOW_ALTO, WINDOW_ANCHO, canales = frame.shape
    if res.multi_hand_landmarks:
        for puntos in res.multi_hand_landmarks:
            # mp_dibujo.draw_landmarks(frame, puntos, mp_manos.HAND_CONNECTIONS)
            fingers["pulgar"] = puntos.landmark[4]
            fingers["indice"] = puntos.landmark[8]
            fingers["medio"] = puntos.landmark[12]
            fingers["anular"] = puntos.landmark[16]
            fingers["menique"] = puntos.landmark[20]
            punto_central["cords"] = puntos.landmark[5]
            punto_central["width"] = calcCoordsY(punto_central["cords"])
            punto_central["height"] = calcCoordsX(punto_central["cords"])
            aux = []
            count = 0
            for finger in fingers:
                if (
                    finger != "pulgar"
                    and calcCoordsY(fingers[finger]) < punto_central["width"]
                ):
                    aux.append(FINGERS[count])
                count += 1
            if calcCoordsX(fingers["pulgar"]) < punto_central["height"]:
                aux.append("Pulgar")
            UP_FINGERS = aux
        # print(len(UP_FINGERS))
        if len(UP_FINGERS) == 5:
            FINAL_TEXT = "Mano Extendida"
        elif UP_FINGERS.count("Pulgar") == 1:
            FINAL_TEXT = "Pulgar Arriba"
        else:
            FINAL_TEXT = "..."
        ocv.putText(
            frame, FINAL_TEXT, (50, 50), ocv.FONT_ITALIC, 2, (0, 56, 255), thickness=3
        )
    else:
        ocv.putText(
            frame,
            "No hay manos",
            (50, 50),
            ocv.FONT_ITALIC,
            2,
            (0, 56, 255),
            thickness=3,
        )

    ocv.imshow(WINDOW_NAME, frame)
    salir = ocv.waitKey(1)
    if salir == 27:
        break

cap.release()
ocv.destroyAllWindows()
