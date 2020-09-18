import os.path
from os import path
import glob

# Set to 1 for success messages. 
verbose = 1

# Checks if a directory contains the correct number of .PNGs. 
def png_checker(path, images_required):
    images = len(glob.glob1(path,'*.png'))
    if images != images_required:
        print(path + ' is INVALID! Contains ' + str(images) + ' images instead of ' + str(images_required) + ' images.')
    elif verbose:
        print(path + ' is COMPLETE.')
# Checks if single directory datasets are complete. 
def directory_checker(dataset, images):    
    dataset_path = 'data/' + dataset
    print('\nChecking ' + dataset + ' dataset...')
    if path.exists(dataset_path):
        png_checker(dataset_path, images)
    else:
        print(dataset + ' is MISSING!')

print('DATA CHECKER')

# Check if BSDS100 is a complete dataset. 
directory_checker('BSDS100', 100)

# Check if BSDS200 is a complete dataset. 
directory_checker('BSDS200', 200)

# Check if DIV2K is a complete dataset. 
print('\nChecking DIV2K dataset...')
dataset_path = 'data/DIV2K'
if path.exists(dataset_path):
    # Check if DIV2K contains all required low-resolution subsets.
    subsets_LR = ['DIV2K_train_LR_bicubic', 'DIV2K_train_LR_unknown', 'DIV2K_valid_LR_bicubic', 'DIV2K_valid_LR_unknown']
    for subset in subsets_LR:
        subset_path = dataset_path + '/' + subset
        if path.exists(subset_path):
            # Check if each subset contains all required scales. 
            scales = ['X2', 'X3', 'X4']
            for scale in scales:
                scale_path = subset_path + '/' + scale
                if path.exists(scale_path):
                    # Check each scale contains the required number of images. 
                    if scale_path.find('train') != -1:
                        png_checker(scale_path, 800)
                    # Valid datasets contain 100 images. 
                    else:
                        png_checker(scale_path, 100)
                else:
                    print(scale_path + ' is MISSING!')
        else:
            print(subset_path + ' is MISSING!')
    # Check if DIV2K contains all required high-resolution subsets.
    subsets_HR = ['DIV2K_train_HR', 'DIV2K_valid_HR']
    for subset in subsets_HR:
        subset_path = dataset_path + '/' + subset
        if path.exists(subset_path):
            # Check if each subset contains the required number of images. 
            if subset_path.find('train') != -1:
                png_checker(subset_path, 800)
            # Valid datasets contain 100 images. 
            else:
                png_checker(subset_path, 100)
        else:
            print(subset_path + ' is MISSING!')
else:
    print('DIV2K is MISSING!')

# Check if General100 is a complete dataset. 
directory_checker('General100', 100)

# Check if historical is a complete dataset. 
print('\nChecking historical dataset...')
dataset_path = 'data/historical/LR'
if path.exists(dataset_path):
    png_checker(dataset_path, 10)
else:
    print(historical + ' is MISSING!')
    
# Check if manga109 is a complete dataset. 
directory_checker('manga109', 109)    

# Check if T91 is a complete dataset. 
directory_checker('T91', 91)    

# Check if urban100 is a complete dataset. 
directory_checker('urban100', 100)   