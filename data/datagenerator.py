import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.utils.data_utils import Sequence
import numpy as np
from sys import maxsize
from dictionary import testing_dict, training_dict

# Generates batches of LR and HR pairs
class DataGenerator(Sequence):
    #list_IDs is the images 
    def __init__(self, scale, batch_size, dictionary = "train", shuffle=True):
        'Initialization'
        if dictionary == "test":
          self.images = testing_dict()
        else:
          self.images = training_dict()
        self.scale = scale
        self.r = int(scale[-1])
        self.list_IDs = list(self.images.keys())
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.on_epoch_end()

    def __len__(self):
        'denotes the number of batches per epoch'
        return int(np.floor(len(self.list_IDs) / self.batch_size))

    def __getitem__(self, index):
        'Makes one batch of data'
        indexes = self.indexes[index*self.batch_size: (index+1)*self.batch_size] 
        list_IDs_temp = [self.list_IDs[k] for k in indexes] 
        # generate data
        X = self.__data_generation(list_IDs_temp)
        return X

    def on_epoch_end(self):
        'Updates indexes after each epoch'
        self.indexes = np.arange(len(self.list_IDs))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)

    def __data_generation(self, list_IDs_temp):
        'Generates data containing batch_size samples' 
        LR = []
        HR = []
        min_height_LR = maxsize
        min_width_LR = maxsize
        # Append images as arrays to LR and HR
        for ID in list_IDs_temp:
            low_res = keras.preprocessing.image.load_img(self.images[ID][self.scale])
            high_res = keras.preprocessing.image.load_img(self.images[ID]['original'])
            low_res = np.asarray(low_res)
            high_res = np.asarray(high_res)
            low_res = low_res.astype('float32')
            high_res = high_res.astype('float32')
            # Normalize images to [0,1]
            low_res /= 255.0
            high_res /= 255.0
            LR.append(low_res)
            HR.append(high_res)
            # Find the minimum LR dimensions 
            min_height_LR = min(min_height_LR, low_res.shape[0])
            min_width_LR = min(min_width_LR, low_res.shape[1])
        # HR/SR image is bigger by a factor of r
        min_height_HR = self.r * min_height_LR
        min_width_HR = self.r * min_width_LR
        for i in range (0, len(LR)):
            # Crop LR and HR images to have the same dimensions 
            LR[i] = self.crop_corner(LR[i], min_width_LR, min_height_LR)
            HR[i] = self.crop_corner(HR[i], min_width_HR, min_height_HR)
        LR = np.asarray(LR)
        HR = np.asarray(HR)    
        return LR, HR 
    
    def crop_center(self, img, min_width, min_height):        
        'Crops image around the center given minimum width and height'
        width = img.shape[1]
        height = img.shape[0]
        # Calculates new boundaries around the center
        left = int(np.ceil((width - min_width) / 2))
        right = left + min_width
        top = int(np.ceil((height - min_height) / 2))
        bottom = top + min_height
        # Crop original image
        cropped_img = img[top:bottom, left:right, ...]
        return cropped_img

    def crop_corner(self, img, min_width, min_height):        
        # Crops from top left corner
        cropped_img = img[0:min_height, 0:min_width, ...]
        return cropped_img