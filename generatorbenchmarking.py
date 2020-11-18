import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import time
import datagenerator
from datagenerator import DataGenerator
start_time = time.time()
size = 5
testing_generator = DataGenerator('LRbicx' + str(3), batch_size = size, dictionary = "test")
print("---%s seconds --- " % (time.time() - start_time))
for x in range(size):
    lr, hr = testing_generator.__getitem__(x)
    fig = plt.figure()
    fig.set_size_inches(10, 10)
    ax1 = fig.add_subplot(1,2,1)
    ax1.set_title('Low Resolution (LR): ' + str(lr[0].shape[0]) + ' x ' + str(lr[0].shape[1]) + ' pixels')
    ax1.imshow(lr[0])
    ax2 = fig.add_subplot(1,2,2)
    ax2.set_title('High Resolution (HR): ' + str(hr[0].shape[0]) + ' x ' + str(hr[0].shape[1]) + ' pixels')
    ax2.imshow(hr[0])
    plt.show()
