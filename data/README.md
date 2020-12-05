# Data
This directory contains the datasets, the scripts to download and process them, and the Keras data generator. Refer to the directions in **Assemble the Dataset**.
#### `datasets/`
Follow the directions in **Assemble the Dataset**. All of the images used in this project are stored here.
#### [`__init__.py`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/data/__init__.py)
Marks this directory as the package `data`. Includes the `DataGenerator` class.
#### [`augument.py`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/data/augment.py)
The class `DataAugmentor` can rotate, flip, and crop batches of images. It is currently unused. 
#### [`benchmark.py`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/data/benchmark.py)
Measures the time that it takes for `DataGenerator` to generate batches of images. 
#### [`check.py`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/data/check.py)
Checks if `datasets/` follows the file structure, which is defined in the section **Required File Structure**, required by [`process.m`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/data/process.m). Use `python check.py` for verbose output, or use `python check.py off` to only display errors. 
#### [`dictionary.py`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/data/dictionary.py)
Contains `training_dict()`, which returns a dictionary of all of the filepaths in the DIV2K dataset, and `testing_dict()`, which returns a dictionary of all of the filepaths in the Classical SR dataset, to be used by the `DataGenerator`. The dictionary is formatted as `{image_name:{scale:filepath}}`. Important note: This file is designed to be run from the main directory. If running from this directory, remove the `'data/'` prefix `main_dir` and `data_directory`.
#### [`download.py`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/data/download.py)
Follow the directions in **Assemble the Dataset**. Downloads the Classical SR and DIV2K datasets, unzips them, and assembles the required data structure. 
#### [`generator.py`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/data/generator.py)
Contains the Keras `DataGenerator` class, which outputs batches of low resolution and high resolution images. It is used for all training and testing in this project and can be initialized as an object through `DataGenerator(scale, batch_size, dictionary = "train", shuffle = True).` Important note: this file uses [`dictionary.py`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/data/dictionary.py) to find images. 
#### [`process.m`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/data/process.m)
MATLAB script that uses bicubic degradation to downscale images and move them into the file structure used by `dictionary.py`. Must follow the file structure defined in **Required File Structure** to work properly. Only run this after verifying that [`check.py`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/data/check.py) displays no errors.
## Assemble the Dataset
The dataset used by the `DataGenerator` can be assembled by following either of the following sets of directions. 
### Directions ([`download.py`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/data/download.py) Method)
1. Run `python download.py` to download all required data. `check.py` is run at the end to verify that all datasets are complete. 
2. If `python check.py off` displays no errors, then run [`process .m`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/data/process.m) in MATLAB to process the images into the required dataset. 
### Directions (Manual Method)
1. Create a directory named `datasets/` in this folder (filepath `data/datasets/`).
2. Download all .zip files in the [Classical SR Google Drive](https://drive.google.com/drive/folders/1pRmhEmmY-tPF7uH8DuVthfHoApZWJ1QU). Unzip them and place their contents in `datasets/`. 
3. Create a directory named `DIV2K/` in `datasets/` (filepath `data/datasets/DIV2K/`). Download the all of the .zip files under "(NITRE 2017) Low Res Images" and "High Resolution Images" sections of the [DIV2K Dataset website](https://data.vision.ee.ethz.ch/cvl/DIV2K/). Unzip all of them inside of `DIV2K/`. 
4. Run `python check.py off`. If no errors are displayed, , then run [`process .m`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/data/process.m) in MATLAB to process the images into the required dataset. 
## Dataset Information
The only datasets used in this project are Classical SR and DIV2K. However, these datasets may be useful for future research. A description of all of the required and supplementary datasets can be found [here](https://cvnote.ddlee.cn/2019/09/22/image-super-resolution-datasets).
* Classical SR: [Google Drive](https://drive.google.com/drive/folders/1pRmhEmmY-tPF7uH8DuVthfHoApZWJ1QU)
* DIV2K: [Website](https://data.vision.ee.ethz.ch/cvl/DIV2K/)
* 2K Resolution: [Google Drive](https://drive.google.com/drive/folders/1B-uaxvV9qeuQ-t7MFiN1oEdA6dKnj2vW) 
* Outdoor Scene: [Google Drive](https://drive.google.com/drive/u/0/folders/1iZfzAxAwOpeutz27HC56_y5RNqnsPPKr)
* PRIM: [Google Drive](https://drive.google.com/drive/folders/17FmdXu5t8wlKwt8extb_nQAdjxUOrb1O)
* Flickr1024: [Google Drive](https://drive.google.com/drive/folders/10LTXCSp9UqY9A9HVj3sAf7zmS4KdJo2T), [GitHub](https://yingqianwang.github.io/Flickr1024/)
* Multi-Sensor Datasets: [Website](https://www5.cs.fau.de/research/data/multi-sensor-super-resolution-datasets/)
## Required File Structure
`datasets/` must follow the required file structure for [`process.m`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/data/process.m) to run correctly. [`check.py`](https://github.com/umd-fire-coml/2020-Image-Super-Resolution/blob/master/data/check.py) checks if this file structure is satisfied. 
```
datasets/
  BSDS100/
  BSDS200/
  DIV2K/
    DIV2K_train_HR/
    DIV2K_train_LR_bicubic/
      X2/
      X3/
      X4/
    DIV2K_train_LR_unknown/
      X2/
      X3/
      X4/
    DIV2K_valid_HR/
    DIV2K_valid_LR_bicubic/
      X2/
      X3/
      X4/
    DIV2K_valid_LR_unknown/
      X2/
      X3/
      X4/
  General100/
  historical/
    LR/
  manga109/
  Set5/
    GTmod12/
    LRbicx2/
    LRbicx3/
    LRbicx4/
    original/
  Set14/
    GTmod12/
    LRbicx2/
    LRbicx3/
    LRbicx4/
    original/
  T91/
  urban100/
  ```
