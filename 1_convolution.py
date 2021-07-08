import numpy as np
from PIL import Image as img
import tensorflow as tf 

tensarray = np.ones((6,3))*200
zeroarray = np.zeros((6,3))

# This is an image array
imagearray = np.concatenate((tensarray,zeroarray),axis=1).astype(np.uint8)

# This is vertical edge filter
vert_filter = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])

# This is to visualize how image is formed
image = img.fromarray(imagearray)
# image.save("1.png")


convImg = np.zeros((4,4))
resultImg = tf.nn.conv2d(input=imagearray,filters=vert_filter,strides=1,padding=1)
print(resultImg)