# Hue, Saturation, Value
# Matiz, Saturation, Brillo
import cv2 as ocv
import matplotlib.pyplot as plt
IMAGEN = "./img/batman.jpg"

img = ocv.imread(IMAGEN)
img = ocv.cvtColor(img, ocv.COLOR_BGR2RGB)
imgHSV = ocv.cvtColor(img, ocv.COLOR_BGR2HSV)
Hue,Saturation, Value = ocv.split(imgHSV)

fig = plt.figure(figsize=(12,3))

# Hue => Color
hue = fig.add_subplot(1,4,1)
hue.imshow(Hue, cmap="gray")
hue.set_title("Canal H")
# Saturation => Intensidad
sat = fig.add_subplot(1,4,2)
sat.imshow(Saturation, cmap="gray")
sat.set_title("Canal S")
# Value => Brillo
val = fig.add_subplot(1,4,3)
val.imshow(Value, cmap="gray")
val.set_title("Canal V")

#Imagen
imag = fig.add_subplot(1,4,4)
imag.imshow(img)
imag.set_title("Imagen")

""" 
ocv.merge(Hue,Saturation,Value) 

"""

plt.show()