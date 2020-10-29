# Image Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network (ESPCN)
[Paper](https://arxiv.org/pdf/1609.05158.pdf)
## Input
The model is trained using low-resolution (LR) images from the DIV2K dataset that were downscaled with bicubic degradation. datagenerator.py contains the DataGenerator class, which generates batches of LR and high-resolution (HR) image pairs for training and testing. Each LR image is directly fed to the network for feature extraction. 

The LR input is mathematically represented by <img src="https://latex.codecogs.com/gif.latex?I^{LR}"/> and the HR image that it was downscaled from is <img src="https://latex.codecogs.com/gif.latex?I^{HR}"/>. <img src="https://latex.codecogs.com/gif.latex?r"/> is the factor by which the HR image was downsampled by to create the LR image; it is also referenced to as the upscale ratio because the model upscales the LR image to its original resolution. <img src="https://latex.codecogs.com/gif.latex?I^{LR}"/> and <img src="https://latex.codecogs.com/gif.latex?I^{HR}"/> can be represented as real-valued tensors of size <img src="https://latex.codecogs.com/gif.latex?H*W*C"/> and <img src="https://latex.codecogs.com/gif.latex?rH*rW*C"/>, respectively, where <img src="https://latex.codecogs.com/gif.latex?H"/> is the height of the LR image, <img src="https://latex.codecogs.com/gif.latex?W"/> is the width of the LR image, and <img src="https://latex.codecogs.com/gif.latex?C"/> is the number of color channels. 
## Convolutional Neural Network
In our architecture, a seven layer convolutional neural network is applied directly to the LR image to produce the SR image. The first six layers extract feature maps from the LR image and the seventh is a sub-pixel convolution layer that upscales the LR feature maps to produce the SR image, <img src="https://latex.codecogs.com/gif.latex?I^{SR}"/>.
### Feature Map Extraction
The six convolutions are used to extract feature maps from the LR image and can be described as follows: 

<img src="https://latex.codecogs.com/gif.latex?f^1(I^{LR};W_1,b_1)=\phi(W_1*I^{LR}+b_1)"/>

<img src="https://latex.codecogs.com/gif.latex?f^2(I^{LR};W_{1:2},b_{1:2})=\phi(W_2*f^1(I^{LR})+b_2)"/>

<img src="https://latex.codecogs.com/gif.latex?f^3(I^{LR};W_{1:3},b_{1:3})=\phi(W_3*f^2(I^{LR})+b_3)"/>

<img src="https://latex.codecogs.com/gif.latex?f^4(I^{LR};W_{1:4},b_{1:4})=\phi(W_4*f^3(I^{LR})+b_4)"/>

<img src="https://latex.codecogs.com/gif.latex?f^5(I^{LR};W_{1:5},b_{1:5})=\phi(W_5*f^4(I^{LR})+b_5)"/>

<img src="https://latex.codecogs.com/gif.latex?f^6(I^{LR};W_{1:6},b_{1:6})=\phi(W_6*f^5(I^{LR})+b_6)"/>

Where <img src="https://latex.codecogs.com/gif.latex?W_l,b_l,l\in(1,7)"/> are learnable network weights and biases respectively. <img src="https://latex.codecogs.com/gif.latex?W_l"/> is a 2D convolution tensor of size <img src="https://latex.codecogs.com/gif.latex?n_{l-1}*n_l*k_l*k_l"/>, where <img src="https://latex.codecogs.com/gif.latex?n_l"/> is the number of features at layer <img src="https://latex.codecogs.com/gif.latex?l"/>, <img src="https://latex.codecogs.com/gif.latex?n_0=C"/>, and <img src="https://latex.codecogs.com/gif.latex?k_l"/> is the filter size at layer <img src="https://latex.codecogs.com/gif.latex?l"/>. The activation function <img src="https://latex.codecogs.com/gif.latex?\phi"/> is applied element-wise and is fixed.

## Efficient Sub-Pixel Convolutional Layer

## Output
The output is a super-resolution (SR) image that is compared to the HR image in testing. 
