import os 

data_directory = 'data/'
datasets = ['BSDS100', 'BSDS200', 'General100', 'historical', 'manga109', 'Set5', 'Set14', 'T91', 'urban100']
scales = ['LRbicx2', 'LRbicx3', 'LRbicx4']

# key = image name without directory path
# value = dict of filepaths of original and scaled images
images = {}
# Build images dict for all classical SR images
for dataset in datasets:
    dataset_directory = data_directory + dataset + '/'
    # Get list of all image names
    image_names = os.listdir(dataset_directory + 'original')
    for image_name in image_names:
        # image_scales dict for storing filepaths of original and scaled images
        # key = scale
        # value = filepath of image
        image_scales = {}
        # original filepath
        image_scales['original'] = dataset_directory + 'original/' + image_name
        # scaled filepaths
        for scale in scales:
            image_scales[scale] = dataset_directory + scale + '/' + image_name
        # image name points to dictionary of scales
        images[image_name] = image_scales

# file_path = images[<image name>][<scale>]

main_dir = 'data/DIV2K'
Kscale = ['KX2', 'KX3', 'KX4']
Uscale = ['UX2', 'UX3', 'UX4']


train_names = os.listdir(main_dir + '/' + 'DIV2K_train_HR')
valid_names = os.listdir(main_dir + '/' + 'DIV2K_valid_HR')

for image_name in train_names:
    image_scales = {}
    image_scales['original'] = main_dir + '/' + 'DIV2K_train_HR' + '/' + image_name
    for scale in Kscale:
        s = ''
        if(scale == 'KX2'):
            s = 'x2'
        elif(scale == 'KX3'):
            s = 'x3'
        else:
            s = 'x4'
            
        corr_name = image_name[:4] + s + image_name[4:]
        image_scales[scale] = main_dir + '/' + 'DIV2K_train_LR_bicubic' + '/' + corr_name
    for scale in Uscale:
        s = ''
        if(scale == 'UX2'):
            s = 'x2'
        elif(scale == 'UX3'):
            s = 'x3'
        else:
            s = 'x4'
            
        corr_name = image_name[:4] + s + image_name[4:]
        image_scales[scale] = main_dir + '/' + 'DIV2K_train_LR_unknown' + '/' + corr_name
    images[image_name] = image_scales
for image_name in valid_names:
    image_scales = {}
    image_scales['original'] = main_dir + '/' + 'DIV2K_valid_HR' + '/' + image_name
    for scale in Kscale:
        s = ''
        if(scale == 'KX2'):
            s = 'x2'
        elif(scale == 'KX3'):
            s = 'x3'
        else:
            s = 'x4'
            
        corr_name = image_name[:4] + s + image_name[4:]
        image_scales[scale] = main_dir + '/' + 'DIV2K_valid_LR_bicubic' + '/' + corr_name
    for scale in Uscale:
        s = ''
        if(scale == 'UX2'):
            s = 'x2'
        elif(scale == 'UX3'):
            s = 'x3'
        else:
            s = 'x4'
            
        corr_name = image_name[:4] + s + image_name[4:]
        image_scales[scale] = main_dir + '/' + 'DIV2K_valid_LR_unknown' + '/' + corr_name        
    images[image_name] = image_scales


