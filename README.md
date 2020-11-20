# Single Image Super-Resolution Using a Seven-Layer Efficient Sub-Pixel Convolutional Neural Network
Super-resolution is the process of recovering a high resolution (HR) image or video from its low resolution (LR) counterpart. It has a myriad of applications in many fields, including autonomous vehicles, medical imaging, security, and entertainment. 

![diagram](https://www.mathworks.com/help/examples/deeplearning_shared/win64/VeryDeepSuperResolutionDeepLearningExample_01.png)

Machine learning super resolution uses a model trained with a dataset of images to predict additional pixels from a LR image input, essentially "filling in" the gaps in between the pixels of a LR image to create a HR output. We refer to a recovered HR image as a super-resolved (SR) image. A SR image has more pixels than the LR image that it was created from, so it contains more information and will be appear clearer due to its higher pixel density.

Our model uses a series of convolutional layers to extract, or learn, information from the LR image. Then, it combines the data that it collected to create the SR image. In technical terms, this is a seven-layer Efficient Sub-Pixel Convolutional Neural Network that takes a LR image input, extracts LR feature maps through a series of convolutional layers, then applies a sub-pixel convolution layer to assemble the LR feature maps into a HR image output. This project is written in TensorFlow and is based on [Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network](https://arxiv.org/pdf/1609.05158.pdf). 

## Interactive Notebook and Demonstration Video
[![Demonstration Video](https://i.imgur.com/My80T83.png)](https://www.youtube.com/watch?v=KnT1GiVU8O4)

Learn about this project and use a trained model without any setup by visiting our [Interactive Notebook](https://drive.google.com/file/d/1d-1gZsZnIza1KMHSWT0G3tiDAHePZyUR/view?usp=sharing), hosted by Google Colab. Watch our demonstration video on YouTube for a high-level walkthrough and explanation of our project.
## Project Setup
1. Clone this repository.
2. Run `conda env create -f environment.yml` from this directory to create the project environment. Activate it using `conda activate image-super-resolution`.
3. Follow the directions in [`data/`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/tree/respository_organization/data) to assemble the dataset.
4. Refer to **Training** and **Testing** for training and testing the model.
## Model
![architecture](https://miro.medium.com/max/4902/1*n4cXo7DASn1_HEGrDNJVFg.png)
The Efficient Sub-Pixel Convolutional Neural Network (ESPCN) model is a machine learning Single Image Super-Resolution (SISR) model that takes a LR image input, extracts LR feature maps through a series of convolutional layers, then uses a sub-pixel convolution layer to convert the LR feature maps into a HR image output. Refer to [`model/`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/tree/respository_organization/model) for documentation of our model and the Peak Signal to Noise Ratio (PSNR) function.
## Training

## Testing
![example](https://i.imgur.com/K3acirQ.png)
