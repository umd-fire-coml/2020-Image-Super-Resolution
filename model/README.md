# Model
This directory contains the model, PSNR function, and any saved weights. Refer to **Design** for extensive documentation of our model, how we arrived at it, and how it is implemented. 
### [`weights/`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/tree/master/model/weights)
Weights are saved here after the model is finished training. We pre-trained [`r3bs10epochs100weights.h5`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/model/weights/r3bs10epochs100weights.h5) with scale factor 3 and batch size 10 over 100 epochs, which are the values in [`training.ipynb`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/training.ipynb), and included it here for your convenience. These are also the weights that are loaded by default in `testing.ipynb`.
### [`__init__.py`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/model/__init__.py)
Marks this directory as the package `model`. Includes the model as the `espcn` function and the `psnr` function. 
### [`espcn.py`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/model/espcn.py)
TensorFlow implementation of the model described in **Design**. Refer to the "Implementation" section.
### [`psnr.py`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/model/psnr.py)
Peak Signal to Noise Ratio (PSNR) used for testing. Refer to **Peak Signal to Noise Ratio**.
## Design
![architecture](https://miro.medium.com/max/4902/1*n4cXo7DASn1_HEGrDNJVFg.png)
The Efficient Sub-Pixel Convolutional Neural Network (ESPCN) model is a machine learning Single Image Super-Resolution (SISR) model that takes a LR image input, extracts LR feature maps through a series of convolutional layers, then uses a sub-pixel convolution layer to convert the LR feature maps into a HR image output. In our architecture, a seven layer convolutional neural network is applied directly to the LR image to produce the SR image. The first six layers extract feature maps from the LR image and the seventh is a sub-pixel convolution layer that upscales the LR feature maps to produce a HR image, ![equation](https://latex.codecogs.com/gif.latex?I^{SR}). 
### Input
LR images are directly fed to the network for feature extraction. The LR input is mathematically represented by ![equation](https://latex.codecogs.com/gif.latex?I^{LR}) and the HR image that it was downscaled from is ![equation](https://latex.codecogs.com/gif.latex?I^{HR}). ![equation](https://latex.codecogs.com/gif.latex?r) is the factor by which the HR image was downsampled by to create the LR image; it is also referenced to as the upscale ratio because the model upscales the LR image to its original resolution. ![equation](https://latex.codecogs.com/gif.latex?I^{LR}) and ![equation](https://latex.codecogs.com/gif.latex?I^{HR}) can be represented as real-valued tensors of size ![equation](https://latex.codecogs.com/gif.latex?H%20%5Ctimes%20W%20%5Ctimes%20C) and ![equation](https://latex.codecogs.com/gif.latex?rH%20%5Ctimes%20rW%20%5Ctimes%20C), respectively, where ![equation](https://latex.codecogs.com/gif.latex?H) is the height of the LR image, ![equation](https://latex.codecogs.com/gif.latex?W) is the width of the LR image, and ![equation](https://latex.codecogs.com/gif.latex?C) is the number of color channels. 
### Feature Maps Extraction
The six convolutional layers that are used to extract feature maps from the LR image can be described as follows: 

![equation](https://latex.codecogs.com/gif.latex?f^1(I^{LR};W_1,b_1)=\phi(W_1*I^{LR}+b_1))

![equation](https://latex.codecogs.com/gif.latex?f^2(I^{LR};W_{1:2},b_{1:2})=\phi(W_2*f^1(I^{LR})+b_2))

![equation](https://latex.codecogs.com/gif.latex?f^3(I^{LR};W_{1:3},b_{1:3})=\phi(W_3*f^2(I^{LR})+b_3))

![equation](https://latex.codecogs.com/gif.latex?f^4(I^{LR};W_{1:4},b_{1:4})=\phi(W_4*f^3(I^{LR})+b_4))

![equation](https://latex.codecogs.com/gif.latex?f^5(I^{LR};W_{1:5},b_{1:5})=\phi(W_5*f^4(I^{LR})+b_5))

![equation](https://latex.codecogs.com/gif.latex?f^6(I^{LR};W_{1:6},b_{1:6})=\phi(W_6*f^5(I^{LR})+b_6))

Where ![equation](https://latex.codecogs.com/gif.latex?W_l,b_l,l\in(1,6)) are learnable network weights and biases, respectively. ![equation](https://latex.codecogs.com/gif.latex?W_l) is a 2D convolution tensor of size ![equation](https://latex.codecogs.com/gif.latex?n_%7Bl-1%7D%20%5Ctimes%20n_l%20%5Ctimes%20k_l%20%5Ctimes%20k_l), where ![equation](https://latex.codecogs.com/gif.latex?n_l) is the number of features at layer ![equation](https://latex.codecogs.com/gif.latex?l), ![equation](https://latex.codecogs.com/gif.latex?n_0=C), and ![equation](https://latex.codecogs.com/gif.latex?k_l) is the filter size at layer ![equation](https://latex.codecogs.com/gif.latex?l). The biases ![equation](https://latex.codecogs.com/gif.latex?b_l) are vectors of length ![equation](https://latex.codecogs.com/gif.latex?n_l). The nonlinearity function, or activation function, ![equation](https://latex.codecogs.com/gif.latex?\phi) is applied element-wise and is fixed.

### Efficient Sub-Pixel Convolutional Layer and Output
The sub-pixel convolution layer that converts the LR feature maps to a HR image, ![equation](https://latex.codecogs.com/gif.latex?I^{SR}), can be described as follows:

![equation](https://latex.codecogs.com/gif.latex?I%5E%7BSR%7D%3Df%5E7%5Cleft%28I%5E%7BLR%7D%5Cright%29%3DPS%5Cleft%28W_7%5Cast%20f%5E6%5Cleft%28I%5E%7BLR%7D%5Cright%29+b_7%5Cright%29)

Where ![equation](https://latex.codecogs.com/gif.latex?PS) is a periodic shuffling operator that rearranges the elements of a ![equation](https://latex.codecogs.com/gif.latex?H%20%5Ctimes%20W%20%5Ctimes%20C%20%5Cdot%20r%5E2) tensor to a tensor of shape ![equation](https://latex.codecogs.com/gif.latex?rH%20%5Ctimes%20rW%20%5Ctimes%20C). Therefore, the convolution operator ![equation](https://latex.codecogs.com/gif.latex?W_7) has shape ![equation](https://latex.codecogs.com/gif.latex?n_6%20%5Ctimes%20r%5E2C%20%5Ctimes%20k_7%20%5Ctimes%20k_7). We do not apply nonlinearity to the outputs of this layer because it produces a HR image from the LR feature maps directly with one upscaling filter for each future map. Periodic shuffling can be avoided in training time if the training data is shuffled to match the output of the layer before ![equation](https://latex.codecogs.com/gif.latex?PS).

### Implementation
The following is [`espcn.py`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/model/espcn.py), a Keras implementation of the seven-layer ESPCN model:
```
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Model

# 6-layer ESPCN SISR model. 
# r = upscale factor, channels = number of color channels
def espcn_model(r, channels = 3):
    # Arguments for Conv2D
    conv_args = {
      "activation": "relu",
      "padding" : "same",
    }
    # Input
    inputs = keras.Input(shape=(None, None, channels))
    # Feature Maps Extraction
    conv1 = layers.Conv2D(64, 5, **conv_args)(inputs)
    conv2 = layers.Conv2D(64, 3, **conv_args)(conv1)
    conv3 = layers.Conv2D(32, 3, **conv_args)(conv2)
    conv4 = layers.Conv2D(32, 3, **conv_args)(conv3)
    conv5 = layers.Conv2D(32, 3, **conv_args)(conv4)
    conv6 = layers.Conv2D(channels*(r*r), 3, **conv_args)(conv5)
    # Efficient Sub-Pixel Convolutional Layer
    outputs = tf.nn.depth_to_space(conv6, r)
    return Model(inputs, outputs)
```
[`generator.py`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/data/generator.py) contains the `DataGenerator` class, which generates batches of LR and HR image pairs. The model can be trained with x2, x3, and x4 LR images from the DIV2K dataset that were downscaled with bicubic degradation and an unknown  method. 

The upscale ratio ![equation](https://latex.codecogs.com/gif.latex?r) is represented by `r` and should reflect the scale of the input provided by the data generator. `channels` is ![equation](https://latex.codecogs.com/gif.latex?C), the number of color channels that the input images, and consequently the output images, have. Our model uses six feature map extraction layers that are implemented using `tensorflow.keras.layers.Conv2D`, which convolutes data from 2D images. `relu` is chosen as the fixed activation function ![equation](https://latex.codecogs.com/gif.latex?\phi) for its performance, but other nonlinearity functions, such as `tanh`, are also acceptable. 

There is no strict requirement regarding the number of filters and the kernel size for each `Conv2D`; through experimentation, the parameters can be tuned to optimize performance. For now, we set ![equation](https://latex.codecogs.com/gif.latex?(f_1,n_1)=(5,64)), ![equation](https://latex.codecogs.com/gif.latex?(f_2,n_2)=(3,64)), ![equation](https://latex.codecogs.com/gif.latex?(f_3,n_3)=(3,32)), ![equation](https://latex.codecogs.com/gif.latex?(f_4,n_4)=(3,32)), ![equation](https://latex.codecogs.com/gif.latex?(f_5,n_5)=(3,32)), and ![equation](https://latex.codecogs.com/gif.latex?(f_6,n_6)=(3,r^2)), where ![equation](https://latex.codecogs.com/gif.latex?f_l) is the `kernel_size` and ![equation](https://latex.codecogs.com/gif.latex?n_l) is the number of `filters` at layer ![equation](https://latex.codecogs.com/gif.latex?l).

The sub-pixel convolution layer is implemented using `tf.nn.depth_to_space`. `depth_to_space` rearranges data from depth, collected by the convolutional layers during feature maps extraction, into blocks of spatial data, the output image ![equation](https://latex.codecogs.com/gif.latex?I^{SR}), as a tensor. The width of the output tensor is `input_depth * block_size` and the height is `input_height * block_size`, so `block_size` is set to `r` in order to upscale the input by the upscale ratio. 

At the end, the model is compiled as a `keras.Model` that takes LR image tensors from `DataGenerator` as input, applies the ESPCN SISR model, then outputs HR image tensors. 
## Peak Signal to Noise Ratio
![example](https://i.imgur.com/ToXzT1w.png)
The Peak Signal to Noise Ratio (PSNR) is the ratio between the maximum possible power of a signal and the power of corrupting noise that affects the fidelity of its representation. In this project, it is a representation of how similar two images are: the higher the value, the closer the distance. A PSNR of 0 indicates that two images are the absolute inverse and -1 is returned if the images are completely identical: while this is theoretically impossible, this feature was included to prevent division by 0. In [`testing.py`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/testing.py), the average PSNR of images super-resolved by the untuned model described in **Design** is 24.08 dB, which is within the acceptable values for wireless transmission quality loss (20 to 25 dB). A more in-depth explanation can be found on [Wikipedia](https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio).
