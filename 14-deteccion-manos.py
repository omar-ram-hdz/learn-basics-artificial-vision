# Media pipe
# =>    Objetos, puntos de interés, clasificación de imágenes, segmentación de imagen

from mediapipe import solutions
import cv2 as ocv

WINDOW_NAME = "Detección de Manos"
ID_CAMERA = 0


def coordsC(finger, alto, ancho):
    return (int(finger.x * ancho), int(finger.y * alto))


mp_draw = solutions.drawing_utils

mp_manos = solutions.hands

objeto_hands = mp_manos.Hands(
    static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5
)

cap = ocv.VideoCapture(ID_CAMERA)
ocv.namedWindow(WINDOW_NAME)
# ocv.resizeWindow(WINDOW_NAME)

while True:
    ret, frame = cap.read()
    bgr_frame = ocv.cvtColor(frame, ocv.COLOR_BGR2RGB)
    res = objeto_hands.process(bgr_frame)
    dedoInd = None
    if res.multi_hand_landmarks:
        for puntos in res.multi_hand_landmarks:
            # mp_draw.draw_landmarks(bgr_frame, punto, mp_manos.HAND_CONNECTIONS)
            dedo_pulgar = puntos.landmark[4]
            dedo_indice = puntos.landmark[8]
            dedo_medio = puntos.landmark[12]
            dedo_anular = puntos.landmark[16]
            dedo_menique = puntos.landmark[20]

            punto_central = puntos.landmark[5]

            alto, ancho, canales = frame.shape

            cordIndY, cordIndX = coordsC(dedo_indice, alto, ancho)
            cordCenY, cordCenX = coordsC(punto_central, alto, ancho)

            ocv.circle(
                frame, coordsC(dedo_pulgar, alto, ancho), 20, (34, 255, 76), thickness=1
            )
            ocv.circle(
                frame, coordsC(dedo_indice, alto, ancho), 20, (34, 255, 76), thickness=1
            )
            ocv.circle(
                frame, coordsC(dedo_medio, alto, ancho), 20, (34, 255, 76), thickness=1
            )
            ocv.circle(
                frame, coordsC(dedo_anular, alto, ancho), 20, (34, 255, 76), thickness=1
            )
            ocv.circle(
                frame,
                coordsC(dedo_menique, alto, ancho),
                20,
                (34, 255, 76),
                thickness=1,
            )
            ocv.circle(
                frame,
                coordsC(punto_central, alto, ancho),
                20,
                (34, 255, 76),
                thickness=1,
            )

            if cordIndY < cordCenY:
                dedoInd = 1
            else:
                dedoInd = 0
            print(dedoInd)

    # frame = ocv.flip(frame, 1)
    ocv.imshow(WINDOW_NAME, frame)
    salir = ocv.waitKey(1)
    if salir == 27:
        break

cap.release()
ocv.destroyAllWindows()


# TensorFlow
