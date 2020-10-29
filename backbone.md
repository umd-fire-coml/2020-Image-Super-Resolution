# Image Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network (ESPCN)
![architecture](https://miro.medium.com/max/4902/1*n4cXo7DASn1_HEGrDNJVFg.png)
[Paper](https://arxiv.org/pdf/1609.05158.pdf)
## Input
The model is trained using low-resolution (LR) images from the DIV2K dataset that were downscaled with bicubic degradation. `datagenerator.py` contains the `DataGenerator` class, which generates batches of LR and high-resolution (HR) image pairs for training and testing. Each LR image is directly fed to the network for feature extraction. 

The LR input is mathematically represented by ![equation](https://latex.codecogs.com/gif.latex?I^{LR}) and the HR image that it was downscaled from is ![equation](https://latex.codecogs.com/gif.latex?I^{HR}). ![equation](https://latex.codecogs.com/gif.latex?r) is the factor by which the HR image was downsampled by to create the LR image; it is also referenced to as the upscale ratio because the model upscales the LR image to its original resolution. ![equation](https://latex.codecogs.com/gif.latex?I^{LR}) and ![equation](https://latex.codecogs.com/gif.latex?I^{HR}) can be represented as real-valued tensors of size ![equation](https://latex.codecogs.com/gif.latex?H%20%5Ctimes%20W%20%5Ctimes%20C) and ![equation](https://latex.codecogs.com/gif.latex?rH%20%5Ctimes%20rW%20%5Ctimes%20C), respectively, where ![equation](https://latex.codecogs.com/gif.latex?H) is the height of the LR image, ![equation](https://latex.codecogs.com/gif.latex?W) is the width of the LR image, and ![equation](https://latex.codecogs.com/gif.latex?C) is the number of color channels. 
## Convolutional Neural Network
In our architecture, a seven layer convolutional neural network is applied directly to the LR image to produce the SR image. The first six layers extract feature maps from the LR image and the seventh is a sub-pixel convolution layer that upscales the LR feature maps to produce a HR image, ![equation](https://latex.codecogs.com/gif.latex?I^{SR}). 
In this project, convolutional layers are implemented sequentially using `tensorflow.keras.layers.Conv2D`.
### Feature Maps Extraction
The six convolutions are used to extract feature maps from the LR image and can be described as follows: 

![equation](https://latex.codecogs.com/gif.latex?f^1(I^{LR};W_1,b_1)=\phi(W_1*I^{LR}+b_1))

![equation](https://latex.codecogs.com/gif.latex?f^2(I^{LR};W_{1:2},b_{1:2})=\phi(W_2*f^1(I^{LR})+b_2))

![equation](https://latex.codecogs.com/gif.latex?f^3(I^{LR};W_{1:3},b_{1:3})=\phi(W_3*f^2(I^{LR})+b_3))

![equation](https://latex.codecogs.com/gif.latex?f^4(I^{LR};W_{1:4},b_{1:4})=\phi(W_4*f^3(I^{LR})+b_4))

![equation](https://latex.codecogs.com/gif.latex?f^5(I^{LR};W_{1:5},b_{1:5})=\phi(W_5*f^4(I^{LR})+b_5))

![equation](https://latex.codecogs.com/gif.latex?f^6(I^{LR};W_{1:6},b_{1:6})=\phi(W_6*f^5(I^{LR})+b_6))

Where ![equation](https://latex.codecogs.com/gif.latex?W_l,b_l,l\in(1,7)) are learnable network weights and biases respectively. ![equation](https://latex.codecogs.com/gif.latex?W_l) is a 2D convolution tensor of size ![equation](https://latex.codecogs.com/gif.latex?n_%7Bl-1%7D%20%5Ctimes%20n_l%20%5Ctimes%20k_l%20%5Ctimes%20k_l), where ![equation](https://latex.codecogs.com/gif.latex?n_l) is the number of features at layer ![equation](https://latex.codecogs.com/gif.latex?l), ![equation](https://latex.codecogs.com/gif.latex?n_0=C), and ![equation](https://latex.codecogs.com/gif.latex?k_l) is the filter size at layer ![equation](https://latex.codecogs.com/gif.latex?l). The non-linearity function, or activation function, ![equation](https://latex.codecogs.com/gif.latex?\phi) is applied element-wise and is fixed.

The hyperbolic tangent activation function (`activation = "tanh"`) is used as the fixed non-linearity function in our implementation. 

`TODO: Find (f1,n1), (f2,n2), etc.`
`conv1 = layers.Conv2D(n1, f1, **params)(LR), conv2 = layers.Conv2D(n2, f2, **params)(conv1), etc.)`

### Efficient Sub-Pixel Convolutional Layer
The sub-pixel convolution layer that converts the LR feature maps to a HR image, ![equation](https://latex.codecogs.com/gif.latex?I^{SR}), can be described as follows:

![equation](https://latex.codecogs.com/gif.latex?I%5E%7BSR%7D%3Df%5E7%5Cleft%28I%5E%7BLR%7D%5Cright%29%3DPS%5Cleft%28W_7%5Cast%20f%5E6%5Cleft%28I%5E%7BLR%7D%5Cright%29+b_7%5Cright%29)

Where ![equation](https://latex.codecogs.com/gif.latex?PS) is a periodic shuffling operator that rearranges the elements of a ![equation](https://latex.codecogs.com/gif.latex?H%20%5Ctimes%20W%20%5Ctimes%20C%20%5Cdot%20r%5E2) tensor to a tensor of shape ![equation](https://latex.codecogs.com/gif.latex?rH%20%5Ctimes%20rW%20%5Ctimes%20C). Therefore, the convolution operator ![equation](https://latex.codecogs.com/gif.latex?W_7) has shape ![equation](https://latex.codecogs.com/gif.latex?n_6%20%5Ctimes%20r%5E2C%20%5Ctimes%20k_7%20%5Ctimes%20k_7). We do not apply nonlinearity to the outputs of this layer because it produces a HR image from the LR feature maps directly with one upscaling filter for each future map. Periodic shuffling can be avoided in training time if the training data is shuffled to match the output of the layer before ![equation](https://latex.codecogs.com/gif.latex?PS).

We set `filters` to ![equation](https://latex.codecogs.com/gif.latex?r^2) and use `activation = "sigmoid"` in our implementation.

`TODO: Find f6.`
## Output
`tf.nn.depth_to_space` is used on the seventh layer with `block_size = r` to convert the final convolution to the output image.
