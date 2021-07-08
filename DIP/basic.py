import numpy as np 
from PIL import Image

# OPEN WILL OPEN THE IMAGE AND ASARRAY WILL CONVERT IMG TO NUMPY ARRAY 
img = Image.open("lena.jpg")
print(img)
imgArray = np.asarray(img)

# THIS WILL CONVERT ARRAY BACK TO IMAGE 
data = Image.fromarray(imgArray)
# data.save("newimg.png")
# data.show()

# ARRAY TO IMAGE
rawimg = np.array([[1,2,3],[255,0,200],[120,220,230]]).astype(np.uint8)
print(rawimg)
img = Image.fromarray(rawimg)
img.show()
# img.save("test.png")