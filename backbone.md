# Image Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network (ESPCN)
[Paper](https://arxiv.org/pdf/1609.05158.pdf)
## Input
The model is trained using low-resolution (LR) images from the DIV2K dataset that were downscaled with bicubic degredation. datagenerator.py contains the DataGenerator class, which generates batches of LR and high-resolution (HR) image pairs for training and testing. Each LR image is directly fed to the network for feature extraction. 

The LR input is mathematically represented by <img src="https://latex.codecogs.com/gif.latex?I^{LR}"/> and the HR image that it was downscaled from is <img src="https://latex.codecogs.com/gif.latex?I^{HR}"/>. <img src="https://latex.codecogs.com/gif.latex?r"/> is the factor by which the HR image was downsampled by to create the LR image; it is also referenced to as the upscale ratio because the model upscales the LR image to its original resolution. <img src="https://latex.codecogs.com/gif.latex?I^{LR}"/> and <img src="https://latex.codecogs.com/gif.latex?I^{HR}"/> can be represented as real-valued tensors of size <img src="https://latex.codecogs.com/gif.latex?H*W*C"/> and <img src="https://latex.codecogs.com/gif.latex?rH*rW*rC"/>, respectively, where <img src="https://latex.codecogs.com/gif.latex?C"/> is the number of color channels. 
## Convolutional Neural Network
In our architecture, a seven layer convolutional neural network is applied directly to the LR image to produce the SR image. The first six layers extract feature maps from the LR image and the seventh layer upscales the LR feature maps to produce the SR image, <img src="https://latex.codecogs.com/gif.latex?I^{SR}"/>.
### Feature Map Extraction
The six convolutions are used to extract feature maps from the LR image and can be described as follows: 

<img src="https://latex.codecogs.com/gif.latex?f^1(I^{LR};W_1,b_1)=\phi(W_1*I^{LR}+b_1)"/>

<img src="https://latex.codecogs.com/gif.latex?f^2(I^{LR};W_{1:2},b{1:2})=\phi(W_2*f^1(I^{LR})+b_2)"/>

## Efficient Sub-Pixel Convolutional Layer

## Output
The output is a super-resolution (SR) image that is compared to the HR image in testing. 
