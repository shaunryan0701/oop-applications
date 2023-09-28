import numpy as np
from PIL import Image

# create a 3d numpy array of zeroes, then replace zeroes (black pixels
#  with yellow pixels

data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255,255, 0]
print(data)