# Single Image Super-Resolution Using a Seven-Layer Efficient Sub-Pixel Convolutional Neural Network
Super-resolution is the process of recovering a high resolution (HR) image or video from its low resolution (LR) counterpart. It has a myriad of applications in many fields, including autonomous vehicles, medical imaging, security, and entertainment. 

![diagram](https://www.mathworks.com/help/examples/deeplearning_shared/win64/VeryDeepSuperResolutionDeepLearningExample_01.png)

Machine learning super resolution uses a model trained with a dataset of images to predict additional pixels from a LR image input, essentially "filling in" the gaps in between the pixels of a LR image to create a HR output. We refer to a recovered HR image as a super-resolved (SR) image. A SR image has more pixels than the LR image that it was created from, so it contains more information and will be appear clearer due to its higher pixel density.

Our machine learning project uses a seven-layer Efficient Sub-Pixel Convolutional Neural Network to upscale an image to three times its original resolution. This machine learning model extracts feature maps from the low resolution image through a series of six convolutional layers, then applies a sub-pixel convolution layer to assemble them into a super-resolved image. This project is based on [Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network](https://arxiv.org/pdf/1609.05158.pdf). 

## Interactive Notebook and Demonstration Video
[![Demonstration Video](https://i.imgur.com/My80T83.png)](https://www.youtube.com/watch?v=KnT1GiVU8O4)

Learn about this project and use a trained model without any setup by visiting our [Interactive Notebook](https://drive.google.com/file/d/1d-1gZsZnIza1KMHSWT0G3tiDAHePZyUR/view?usp=sharing) hosted on Google Colab. Watch our YouTube video for a high-level demonstration of the project. 
## Setup

## Training

## Testing
![example](https://i.imgur.com/K3acirQ.png)
