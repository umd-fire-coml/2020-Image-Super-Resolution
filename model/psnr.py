import math
import numpy as np

def psnr(oldimg, newimg):
    # Mean-Squared Error. Represents the distance between images. 
    mse = np.mean((oldimg.astype(float) - newimg.astype(float)) ** 2)
    if mse != 0:
        max_pixel = 1.0
        return 20 * math.log10(max_pixel / math.sqrt(mse))
    else:
        # Prevent division by 0
        return -1 
