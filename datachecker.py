import sys, glob
from os import path

# Checks if a directory contains the correct number of .PNGs. 
def png_checker(path, images_required, verbose):
    images = len(glob.glob1(path,'*.png'))
    if images != images_required:
        print(path + ' is INVALID! Contains ' + str(images) + ' images instead of ' + str(images_required) + ' images.')
    elif verbose:
        print(path + ' is complete.')
# Checks if single directory datasets are complete. 
def directory_checker(dataset, images, verbose):    
    dataset_path = 'data/' + dataset
    if verbose == 1: print('Checking ' + dataset + ' dataset...')
    if path.exists(dataset_path):
        png_checker(dataset_path, images, verbose)
    else:
        print(dataset + ' is MISSING!')

def checker(verbose):
    # Check if BSDS100 is a complete dataset. 
    directory_checker('BSDS100', 100, verbose)

    # Check if BSDS200 is a complete dataset. 
    directory_checker('BSDS200', 200, verbose)

    # Check if DIV2K is a complete dataset. 
    if verbose == 1: print('Checking DIV2K dataset...')
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
                            png_checker(scale_path, 800, verbose)
                        # Valid datasets contain 100 images. 
                        else:
                            png_checker(scale_path, 100, verbose)
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
                    png_checker(subset_path, 800, verbose)
                # Valid datasets contain 100 images. 
                else:
                    png_checker(subset_path, 100, verbose)
            else:
                print(subset_path + ' is MISSING!')
    else:
        print('DIV2K is MISSING!')

    # Check if General100 is a complete dataset. 
    directory_checker('General100', 100, verbose)

    # Check if historical is a complete dataset. 
    if verbose == 1: print('Checking historical dataset...')
    dataset_path = 'data/historical/LR'
    if path.exists(dataset_path):
        png_checker(dataset_path, 10, verbose)
    else:
        print(historical + ' is MISSING!')

    # Check if manga109 is a complete dataset. 
    directory_checker('manga109', 109, verbose)    

    # Check if Set5 is a complete dataset. 
    if verbose == 1: print('Checking Set5 dataset...')
    dataset_path = 'data/Set5'
    if path.exists(dataset_path):
        # Check if DIV2K contains all required low-resolution subsets.
        subsets_LR = ['GTmod12', 'LRbicx2', 'LRbicx3', 'LRbicx4', 'original']
        for subset in subsets_LR:
            subset_path = dataset_path + '/' + subset
            if path.exists(subset_path):
                png_checker(subset_path, 5, verbose)
            else:
                print(subset_path + ' is MISSING!')
    else:
        print('Set5 is MISSING!')

    # Check if Set14 is a complete dataset.
    if verbose == 1: print('Checking Set14 dataset...')
    dataset_path = 'data/Set14'
    if path.exists(dataset_path):
        # Check if DIV2K contains all required low-resolution subsets.
        subsets_LR = ['GTmod12', 'LRbicx2', 'LRbicx3', 'LRbicx4', 'original']
        for subset in subsets_LR:
            subset_path = dataset_path + '/' + subset
            if path.exists(subset_path):
                png_checker(subset_path, 14, verbose)
            else:
                print(subset_path + ' is MISSING!')
    else:
        print('Set14 is MISSING!')

    # Check if T91 is a complete dataset. 
    directory_checker('T91', 91, verbose)    

    # Check if urban100 is a complete dataset. 
    directory_checker('urban100', 100, verbose)   
    
if __name__ == "__main__":    
    print('DATA CHECKER')
    # All messages are shown by default. Success messages can be turned off to make failures easier to read. 
    verbose = 1
    if len(sys.argv) == 2:
        if sys.argv[1] == 'off':
            verbose = 0
    if verbose == 1: print('Run \'python datachecker.py off\' to only show failure messages.')
    if verbose == 0: print('Run \'python datachecker.py\' to show all messages.\nEmpty output means all datasets are complete.')
    checker(verbose)