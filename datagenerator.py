import sys
import os.path
from os import path
import glob  
import cv2
import random

num_size_training_set = 500
training_set = [0 for x in range(num_size_training_set)]

dataset_800_X2 = {'data/DIV2K/DIV2K_train_LR_bicubic/X2', 'data/DIV2K/DIV2K_train_LR_unknown/X2', 'data/Set14/LRbicx2', 'data/Set5/LRbicx2'}
 
dataset_800_X3 = {'data/DIV2K/DIV2K_train_LR_bicubic/X3',  'data/DIV2K/DIV2K_train_LR_unknown/X3', 'data/Set14/LRbicx3', 'data/Set5/LRbicx3'}
 
dataset_800_X4 = {'data/DIV2K/DIV2K_train_LR_bicubic/X4',   'data/DIV2K/DIV2K_train_LR_unknown/X4','data/Set14/LRbicx4', 'data/Set5/LRbicx4'} 
 
dataset_all = {'data/General100', 'data/BSDS100', 'data/urban100', 'data/Set14/GTmod12', 'data/Set14/original', 'data/Set5/GTmod12', 'data/Set5/original', 
                'data/BSDS200',  'data/manga109', 'data/T91','data/historical/LR', 'data/DIV2K/DIV2K_valid_HR'}


#goes through and finds an image of scale X2
def adding_to_the_set1():
    value = randint(1, 4) 
    if(value == 1):
        dataset_path = dataset_800_X2[value] 
        inside_dataset = randint(1,800)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 2):
        dataset_path = dataset_800_X2[value] 
        inside_dataset = randint(1,800)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 3):
        dataset_path = dataset_800_X2[value] 
        inside_dataset = randint(1,14)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 4):
        dataset_path = dataset_800_X2[value] 
        inside_dataset = randint(1, 5)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img

#goes through the datasets and finds an image of scale X3
def adding_to_the_set2():
    value = randint(1, 4) 
    if(value == 1):
        dataset_path = dataset_800_X3[value] 
        inside_dataset = randint(1,800)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 2):
        dataset_path = dataset_800_X3[value] 
        inside_dataset = randint(1,800)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 3):
        dataset_path = dataset_800_X3[value] 
        inside_dataset = randint(1, 14)
         dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 4):
        dataset_path = dataset_800_X3[value] 
        inside_dataset = randint(1, 5)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img

#goes through the datasets and finds an image of scale X4
def adding_to_the_set3():
    value = randint(1, 4) 
    if(value == 1):
        dataset_path = dataset_800_X4[value] 
        inside_dataset = randint(1,800)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 2):
        dataset_path = dataset_800_X4[value] 
        inside_dataset = randint(1,800)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 3):
        dataset_path = dataset_800_X4[value] 
        inside_dataset = randint(1, 14)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 4):
        dataset_path = dataset_800_X4[value] 
        inside_dataset = randint(1, 5)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img

#goes through the datasets and finds an image normally scaled
def adding_to_the_set4():
    value = randint(1, 12) 
    if(value == 1):
        dataset_path = dataset_800_X4[value] 
        inside_dataset = randint(1,100)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 2):
        dataset_path = dataset_all[value] 
        inside_dataset = randint(1,100)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 3):
        dataset_path = dataset_all[value] 
        inside_dataset = randint(1,100)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 4):
        dataset_path = dataset_all[value] 
        inside_dataset = randint(1,14)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img

    elif(value == 5):
        dataset_path = dataset_all[value] 
        inside_dataset = randint(1, 14)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img

    elif(value == 6):
        dataset_path = dataset_all[value] 
        inside_dataset = randint(1, 5)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 7):
        dataset_path = dataset_all[value] 
        inside_dataset = randint(1, 5)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 8):
        dataset_path = dataset_all[value] 
        inside_dataset = randint(1, 200)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 9):
        dataset_path = dataset_all[value] 
        inside_dataset = randint(1, 109)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 10):
        dataset_path = dataset_all[value] 
        inside_dataset = randint(1, 91)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 11):
        dataset_path = dataset_all[value] 
        inside_dataset = randint(1, 10)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img
    elif(value == 12):
        dataset_path = dataset_all[value] 
        inside_dataset = randint(1, 100)
        dir_list = os.listdir(dataset_path) 
        img = dir_list[inside_dataset]
        return img






ind = randint(1,4)
if (ind == 1):
    while len(training_set) < num_size_training_set:
        img = adding_to_the_set1()
        if img not in training_set:
            training_set.append(img)
elif (ind == 2):
    while len(training_set) < num_size_training_set:
        img = adding_to_the_set2()
        if img not in training_set:
            training_set.append(img)
elif (ind == 3):
    while len(training_set) < num_size_training_set:
        img = adding_to_the_set3()
        if img not in training_set:
            training_set.append(img)
if (ind == 4):
    while len(training_set) < num_size_training_set:
        img = adding_to_the_set4()
        if img not in training_set:
            training_set.append(img)


os.mkdir('data/trainingdata')
for x in range(0,num_size_training_set - 1)
    file_path = 'data/trainingdata/' + training_set[x]







