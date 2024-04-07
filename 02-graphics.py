import matplotlib.pyplot as plt
import random

datos = []
for i in range(8):
  datos.append(random.randint(0,10))

print(datos)

plt.figure(figsize=(10,6))

# Graphic
plt.plot(datos, marker="o")
plt.title("Gráfica de 10 datos random")
plt.xlabel("Indice")
plt.ylabel("Valor")

plt.show()