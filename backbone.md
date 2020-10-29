# Image Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network (ESPCN)
[Paper](https://arxiv.org/pdf/1609.05158.pdf)
## Input
The model is trained using low-resolution (LR) images from the DIV2K dataset that were downscaled with bicubic degredation. datagenerator.py contains the DataGenerator class, which generates batches of LR and high-resolution (HR) image pairs for training and testing. Each LR image is directly fed to the network for feature extraction. 
## Feature Maps Extraction
A six layer convolutional neural network is applied directly to the LR image input, which is mathematically represented by <img src="https://latex.codecogs.com/gif.latex?I^{LR}" />.
### Convolutional Layer 1
$`f^1(I^{LR};W_1,b_1)=\theta (W+1*I^{LR}+b_1)`$
## Efficient Sub-Pixel Convolutional Layer

## Output
The output is a super-resolution (SR) image that is compared to the HR image in testing. 
