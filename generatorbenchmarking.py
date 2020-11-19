import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import time
import datagenerator
from datagenerator import DataGenerator

size = 5
image_time = 0
img_time = 0
testing_generator = DataGenerator('LRbicx' + str(3), batch_size = size, dictionary = "test")
start_time = time.time()
for x in range(size):
    lr, hr = testing_generator.__getitem__(x)
    image_time = time.time() 
    for x in range(size):
        fig = plt.figure()
        fig.set_size_inches(10, 10)
        ax1 = fig.add_subplot(1,2,1)
        ax1.set_title('Low Resolution (LR): ' + str(lr[0].shape[0]) + ' x ' + str(lr[0].shape[1]) + ' pixels')
        ax1.imshow(lr[x])
        ax2 = fig.add_subplot(1,2,2)
        ax2.set_title('High Resolution (HR): ' + str(hr[0].shape[0]) + ' x ' + str(hr[0].shape[1]) + ' pixels')
        ax2.imshow(hr[x])
        plt.show()
    image_time = time.time() - image_time
    img_time += image_time
print("---%s seconds --- " % (time.time() - (start_time + img_time)))