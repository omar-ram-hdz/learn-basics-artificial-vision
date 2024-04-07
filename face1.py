import cv2
import mediapipe as mp
import numpy as np

# Inicializar MediaPipe FaceMesh
mp_dibujo = mp.solutions.drawing_utils
mp_cara = mp.solutions.face_mesh

# Asignar el modelo a la variable face_mesh
objeto_cara = mp_cara.FaceMesh(
    static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5
)

# Inicializar la cámara
cap = cv2.VideoCapture(0)

ventana1 = "Facemesh"

count = 0
while True:
    ret, frame = cap.read()  # Capturar un fotograma
    alto, ancho, _ = frame.shape

    # Convertir a formato RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Obtener resultados de la detección de facemesh
    resultados = objeto_cara.process(rgb_frame)
    # Verificar si se detectaron rostros
    if resultados.multi_face_landmarks:
        for puntos in resultados.multi_face_landmarks:

            # Dibujar los landmarks en la cara
            # mp_dibujo.draw_landmarks(frame, puntos, mp_cara.FACEMESH_CONTOURS)
            nariz = puntos.landmark[4]
            frente = puntos.landmark[10]
            barbilla = puntos.landmark[152]
            cX = int(ancho * nariz.x)
            cY = int(alto * nariz.y)
            cXF = int(ancho * frente.x)
            cYF = int(alto * frente.y)
            cXB = int(ancho * barbilla.x)
            cYB = int(alto * barbilla.y)

            p1 = np.array([cXF, cYF])
            p2 = np.array([cXB, cYB])

            l1 = np.linalg.norm(p1 - p2)
            # print(cX, "   ", cY)
            cv2.circle(frame, (cX, cY), 9, (255, 89, 13), thickness=-2)
            cv2.circle(frame, (cXF, cYF), 9, (255, 89, 13), thickness=-2)
            cv2.circle(frame, (cXB, cYB), 9, (255, 89, 13), thickness=-2)
            cv2.line(frame, p1, p2, (9, 200, 255), thickness=8)

            percent = l1 / (alto / 100)
            print(percent)

    # Mostrar el fotograma
    cv2.imshow(ventana1, frame)

    # Salir del bucle si se presiona la tecla 'q'
    salir = cv2.waitKey(1)
    if salir == 27:
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()


""" 
https://github.com/google/mediapipe/blob/master/mediapipe/modules/face_geometry/data/canonical_face_model_uv_visualization.png
"""
""" 
thingiverse
"""
