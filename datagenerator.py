import numpy as np
import keras
import dictionary

class DataGenerator(keras.utils.Sequence):
    #list_IDs is the images 
    def __init__(self, scale, batch_size= 5, shuffle=True):
        'Initialization'
        self.images = dictionary.training_dict()
        self.scale = scale
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

        list_IDs_temp = [self.list_Ids[k] for k in indexes] 

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
        # Initialization
        LR = []
        HR = []
        # Generate data
        for ID in list_IDs_temp:
            low_res = keras.preprocessing.image.load_img(self.images[ID][self.scale])
            high_res = keras.preprocessing.image.load_img(self.images[ID]['original'])
            LR.append(np.asarray(low_res))
            HR.append(np.asarray(high_res))
            
        return LR, HR 

        return X
