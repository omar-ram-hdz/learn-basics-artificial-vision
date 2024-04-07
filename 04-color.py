import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((10,10,3),np.uint8)

# R => Red
img[2,1,0] = 50
img[2,3,0] = 100
img[2,5,0] = 150
img[2,7,0] = 200
img[2,9,0] = 255
# G => Green
img[4,1,1] = 50
img[4,3,1] = 100
img[4,5,1] = 150
img[4,7,1] = 200
img[4,9,1] = 255
# B => Blue
img[6,1,2] = 50
img[6,3,2] = 100
img[6,5,2] = 150
img[6,7,2] = 200
img[6,9,2] = 255


print(img[:,:,0])

plt.imshow(img,cmap="gray")
plt.show()