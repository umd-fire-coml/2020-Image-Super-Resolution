# Datasets
## Directions
1. Run 'python datadownloader.py' to download all required data, or follow the directions in Manually Download Data to manually assemble the required data.

2. Optional step: run 'python datachecker.py' to verify correct file structure. This is performed automatically by datadownloader.py.

3. Run datascaler.m in MATLAB to generate scaled versions of all of the images.


## Manually Download Data
Download all .zip files, unzip them, and assemble the required file structure. Run 'python.datachecker.py' to verify that the data is complete and correct.

#### 1. [Classical SR Training](https://drive.google.com/drive/folders/1pRmhEmmY-tPF7uH8DuVthfHoApZWJ1QU)
Google Drive containing the datasets BSDS100, BSDS200, General100, historical, manga109, Set5, Set14, T91, and urban100.

#### 2. [DIV2K Dataset](https://data.vision.ee.ethz.ch/cvl/DIV2K/)
Download all links under "(NITRE 2017) Low Res Images" and "High Resolution Images" at the bottom of the page.


## Required File Structure
```
data/
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

## Supplementary Information and Datasets
A [description](https://cvnote.ddlee.cn/2019/09/22/image-super-resolution-datasets) of all of the required datasets and some of the supplementary datasets.

The following datasets are not required, but may be useful for further research.

#### 1. [2K Resolution Dataset](https://drive.google.com/drive/folders/1B-uaxvV9qeuQ-t7MFiN1oEdA6dKnj2vW) 

#### 2. [Outdoor Scene Dataset](https://drive.google.com/drive/u/0/folders/1iZfzAxAwOpeutz27HC56_y5RNqnsPPKr)
~30,724 images.

#### 3. [PRIM Dataset](https://drive.google.com/drive/folders/17FmdXu5t8wlKwt8extb_nQAdjxUOrb1O)
400 images.

#### 4. Flickr1024 Dataset
[Google Drive](https://drive.google.com/drive/folders/10LTXCSp9UqY9A9HVj3sAf7zmS4KdJo2T)

[GitHub](https://yingqianwang.github.io/Flickr1024/)

#### 5. [Multi-Sensor Datasets](https://www5.cs.fau.de/research/data/multi-sensor-super-resolution-datasets/)
The first dataset is an indoor scene with ~40 consecutive frames. The second dataset is 6 synthetic datasets, where each dataset consists of 40 frames.
