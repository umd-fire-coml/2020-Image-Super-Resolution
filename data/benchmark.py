from PIL import Image
import numpy as np
import time
from generator import DataGenerator

# Initialize Generator
size = 5
image_time = 0
img_time = 0
testing_generator = DataGenerator('LRbicx' + str(3), batch_size = size, dictionary = "test")
# Start timing
start_time = time.time()
# Generate size images
for x in range(size):
    lr, hr = testing_generator.__getitem__(x)
    image_time = time.time() 
    image_time = time.time() - image_time
    img_time += image_time
# End time and print total time
print("---%s seconds --- " % (time.time() - (start_time + img_time)))
