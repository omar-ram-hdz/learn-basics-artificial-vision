""" 
1) Tarea: 
Crear dos puntos personalizados en el código para dibujar una línea horizontal a partir del Landmark de la nariz, la línea debe medir 100 pixeles hacia la derecha y 100 hacia la izquierda a partir del punto de la nariz, favor de ver la clase grabada a partir de la hora 3 minuto 43 para visualizar la explicación de la tarea.


"""

import numpy as np
import mediapipe as mp
import cv2 as ocv

ID_CAMERA = 0
NAME_WINDOW = "CAPTURA"


mp_dibujo = mp.solutions.drawing_utils
mp_face = mp.solutions.face_mesh

obj_face = mp_face.FaceMesh(
    static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5
)

cap = ocv.VideoCapture(ID_CAMERA)

while True:
    _, frame = cap.read()
    alto, ancho, _ = frame.shape
    rgb_frame = ocv.cvtColor(frame, ocv.COLOR_BGR2RGB)
    res = obj_face.process(rgb_frame)

    if res.multi_face_landmarks:
        for puntos in res.multi_face_landmarks:
            nariz = puntos.landmark[4]
            cX = int(ancho * nariz.x)
            cY = int(alto * nariz.y)

            p1 = np.array([cX - 100, cY])
            p2 = np.array([cX + 100, cY])

            ocv.line(frame, p1, p2, (9, 200, 255), thickness=5)
            ocv.circle(frame, (cX, cY), 9, (255, 89, 13), thickness=-1)
    ocv.imshow(NAME_WINDOW, frame)
    salir = ocv.waitKey(1)
    if salir == 27:
        break

cap.release()
ocv.destroyAllWindows()
