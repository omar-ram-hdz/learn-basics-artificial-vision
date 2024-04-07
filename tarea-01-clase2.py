""" 
1) Tarea: 
Implementar los siguientes códigos: 

• Un código que permita rotar en sentido horario una imagen o video capturado desde la cámara.

• Un código que permita aplicar un efecto espejo a una imagen o video capturado desde la cámara. 

"""
import cv2 as ocv
from tkinter import Tk, Button
import numpy as np

ID_CAMERA = 0
NAME_WINDOW = "CAMARA"
BLACK_PRIMARY = "#222222"
BLACK_SECONDARY = "#1e1e1e"
YELLOW = "#F7DF1E"
RED="#CF3C25"
FONT = ("Arial",15)
ROTATION_X = 0
ROTATION_Y = False
captura = ocv.VideoCapture(ID_CAMERA)
root = Tk()

def setRotation():
  global ROTATION_X
  # ROTATION_X = (ROTATION_X + 1) % 4
  ROTATION_X = ROTATION_X + 45    
  if ROTATION_X >= 315:
    ROTATION_X = 0

def toggleShowWindow():
  global ROTATION_Y
  if ROTATION_Y:
    ROTATION_Y = False
    btn_mirror.config(
      fg=YELLOW,
      text="Ver en espejo"
    )
  else :
    ROTATION_Y = True
    btn_mirror.config(
      fg=RED,
      text="Dejar de ver en Espejo"
    )

root.geometry("300x150")
root.title("{} CONFIG".format(NAME_WINDOW))
root.config(background=BLACK_PRIMARY)

btn_rotate = Button(
  root,
  text="Rotar",
  fg=YELLOW,
  background=BLACK_SECONDARY,
  bg=BLACK_SECONDARY,
  font=FONT,
  command=setRotation,
)
btn_mirror = Button(
  root, 
  text="Ver en espejo",
  fg=YELLOW,
  background=BLACK_SECONDARY,
  bg=BLACK_SECONDARY,
  font=FONT,
  command=toggleShowWindow
)
btn_rotate.pack(pady=10)
btn_mirror.pack(pady=10)

ocv.namedWindow(NAME_WINDOW)

while True:
  ret,frame = captura.read()
  aux = frame
  if ROTATION_Y:
    frame = ocv.flip(frame,1)

  alto,ancho = frame.shape[:2]
  centro = (ancho/2,alto/2)
  m_rotate = ocv.getRotationMatrix2D(centro, ROTATION_X, 1.0)
  frame = ocv.warpAffine(frame, m_rotate, (ancho, alto))
  if ret:
    ocv.imshow(NAME_WINDOW,frame)
    ocv.imshow("ORIGINAL", aux)
  salir = ocv.waitKey(1)
  
  root.update_idletasks()
  root.update()
  
  if salir == 27:
    break

captura.release()
ocv.destroyAllWindows()
root.destroy()
