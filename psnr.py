import numpy as np
import math
# I expect this to be merged in the file with the model


# PSNR stands for Peak Signal to Noise Ratio
# This is a function that will output the PSNR
# of two images, which represents the similarity between
# two images. A higher output represents a more similar image
# The minimum value is 0, representing an absolute inverse
# image while there is no minimum. If two images are identical
# a special case of -1 is returned as the PSNR would otherwise
# be undefined (from a divide by zero)

# mse represents the mean-squared error. This value essentially is a
# representation of how far off two images are from each other. For
# color images, this means the difference between each of the RGB values
# rather than a single value for grayscale.
def psnr(oldimg, newimg):
    mse = np.mean((oldimg.astype(float) - newimg.astype(float)) ** 2)
    if mse != 0:
        max_pixel = 255.0
        return 20 * math.log10(max_pixel / math.sqrt(mse))
    else:
        return -1