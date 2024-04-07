import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((10,10,1),np.uint8)

img[2,1,0] = 50
img[2,3,0] = 100
img[2,5,0] = 150
img[2,7,0] = 200
img[2,9,0] = 255


plt.imshow(img,cmap="gray") # plotear the graphic
#plotear => graphic
plt.show()