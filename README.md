# Single Image Super-Resolution Using a Seven-Layer Efficient Sub-Pixel Convolutional Neural Network
Super-resolution is the process of recovering a high resolution (HR) image or video from its low resolution (LR) counterpart. It has a myriad of applications in many fields, including autonomous vehicles, medical imaging, security, and entertainment. 

![diagram](https://www.mathworks.com/help/examples/deeplearning_shared/win64/VeryDeepSuperResolutionDeepLearningExample_01.png)

Machine learning super resolution uses a model trained with a dataset of images to predict additional pixels from a LR image input, essentially "filling in" the gaps in between the pixels of a LR image to create a HR output. We refer to a recovered HR image as a super-resolved (SR) image. A SR image has more pixels than the LR image that it was created from, so it contains more information and will be appear clearer due to its higher pixel density.

Our model uses a series of convolutional layers to extract, or learn, information from the LR image. Then, it combines the data that it collected to create the SR image. In technical terms, this is a seven-layer Efficient Sub-Pixel Convolutional Neural Network that takes a LR image input, extracts LR feature maps through a series of convolutional layers, then applies a sub-pixel convolution layer to assemble the LR feature maps into a HR image output. This project is written in TensorFlow and is based on [Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network](https://arxiv.org/pdf/1609.05158.pdf). 

## Interactive Notebook and Demonstration Video
[![Demonstration Video](https://i.imgur.com/My80T83.png)](https://i.imgur.com/SNKR8sb.png)

Learn about this project and use a trained model without any setup by visiting our [Interactive Notebook](https://drive.google.com/file/d/1d-1gZsZnIza1KMHSWT0G3tiDAHePZyUR/view?usp=sharing), hosted by Google Colab. Watch our demonstration video on YouTube for a high-level walkthrough and explanation of our project.
## Project Setup
1. Clone this repository.
2. Run `conda env create -f environment.yml` from this directory to create the project environment. Activate it using `conda activate image-super-resolution`.
3. Follow the directions in [`data/`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/tree/respository_organization/data) to assemble the dataset.
4. Refer to **Training** and **Testing** to train and test the model.
## Model
![architecture](https://miro.medium.com/max/4902/1*n4cXo7DASn1_HEGrDNJVFg.png)
The Efficient Sub-Pixel Convolutional Neural Network (ESPCN) model is a machine learning Single Image Super-Resolution (SISR) model that takes a LR image input, extracts LR feature maps through a series of convolutional layers, then uses a sub-pixel convolution layer to convert the LR feature maps into a HR image output. Refer to [`model/`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/tree/respository_organization/model) for documentation of our model and the Peak Signal to Noise Ratio (PSNR) function.
## Training
#### `training.py`
Trains the seven-layer ESPCN model in Keras. The `DataGenerator` loads LR images, all downscaled by `upscale_factor`, and HR images of the original resolution from the training dataset, which consists of images in the DIV2K dataset. Saves the trained weights at `model/weights/r[r]bs[batch_size]epochs[epochs]weights.h5` (e.g. the included pre-trained weights are saved at `model/weights/r3bs10epochs100weights.h5`).

Includes the importable function `train`. Run this script from the console with `python training.py [upscale_factor] [batch_size] [epochs]`. `upscale_factor` is the `r` that the images will be super-resolved with. Batch size is the number of images generated by the DataGenerator in each batch. `epochs` is the number of epochs for which the model will be trained before it is saved. 
#### `training.ipynb`
Shows the model summary and uses `train` to train the model in a Jupyter Notebook.
## Testing
![example](https://i.imgur.com/K3acirQ.png)
#### `testing.py`
Benchmarks a trained model by calculating the average PSNR of 729 inputs. For each image, the `DataGenerator` generates a LR, HR image pair of the model's `upscale_factor` from the testing dataset, which consists of all images in the Classical SR dataset. Then, the LR image is super-resolved to create the SR image and the `psnr` function compares it to the HR image. The average PSNR is calculated and the PSNR of each image can also be optionally shown. 

Includes the importable function `benchmark`. Run this script from the console with `python testing.py [weights_filename] [upscale_factor] [off (optional)]`. `weights_filename` is the filename of trained weights saved in `model/weights` without the directory path (e.g. `r3bs10epochs100weights.h5`). `upscale_factor` is the `r` that the weights were trained to super-resolve the input by. Include `off` to hide output for individual images; otherwise, the PSNR of each image and the cumulative average PSNR at that point will be printed. 
#### `testing.ipynb`
Tests trained models in a Jupyter Notebook. Compiles the model, loads saved weights from the `model/weights`, and initializes the testing `DataGenerator`. Displays the LR, SR, and HR versions of an individual image side-by-side for qualitative comparison and displays the PSNR of the SR and HR images for quantitative comparison. Uses `benchmark` to calculate the average PSNR of the testing dataset. 
