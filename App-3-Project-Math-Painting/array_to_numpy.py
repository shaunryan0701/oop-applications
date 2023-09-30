import numpy as np
from PIL import Image

# create a 3d numpy array of zeroes, then replace zeroes (black pixels
#  with yellow pixels

data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 100, 0]
print(data)

data[1:3] = [255, 0, 0]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')
