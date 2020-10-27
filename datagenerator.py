
class DataGenerator:

    #justins data processor
    def data_processor(self):
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
        Kscale = ['LRbicx2', 'LRbicx3', 'LRbicx4']
        Uscale = ['LRunkx2', 'LRunkx3', 'LRunkx4']

        train_names = os.listdir(main_dir + '/' + 'DIV2K_train_HR')
        valid_names = os.listdir(main_dir + '/' + 'DIV2K_valid_HR')

        for image_name in train_names:
            image_scales = {}
            image_scales['original'] = main_dir + '/' + 'DIV2K_train_HR' + '/' + image_name
            for scale in Kscale:
                s = ''
                sc = ''
                if(scale == 'LRbicx2'):
                    s = 'x2'
                    sc = 'X2'
                elif(scale == 'LRbicx3'):
                    s = 'x3'
                    sc = 'X3'
                else:
                    s = 'x4'
                    sc = 'X4'
            
                corr_name = image_name[:4] + s + image_name[4:]
                image_scales[scale] = main_dir + '/' + 'DIV2K_train_LR_bicubic' + '/' + sc + '/' + corr_name
            for scale in Uscale:
                s = ''
                sc = ''
                if(scale == 'LRunkx2'):
                    s = 'x2'
                    sc = 'X2'
                elif(scale == 'LRunkx3'):
                 s = 'x3'
                 sc = 'X3'
                else:
                 s = 'x4'
                 sc = 'X4'
            
                corr_name = image_name[:4] + s + image_name[4:]
                image_scales[scale] = main_dir + '/' + 'DIV2K_train_LR_unknown' + '/' + sc + '/' + corr_name
            images[image_name] = image_scales
        for image_name in valid_names:
            image_scales = {}
            image_scales['original'] = main_dir + '/' + 'DIV2K_valid_HR' + '/' + image_name
            for scale in Kscale:
                s = ''
                sc = ''
                if(scale == 'LRbicx2'):
                    s = 'x2'
                    sc = 'X2'
                elif(scale == 'LRbicx3'):
                    s = 'x3'
                    sc = 'X3'
                else:
                    s = 'x4'
                    sc = 'X4'
            
                corr_name = image_name[:4] + s + image_name[4:]
                image_scales[scale] = main_dir + '/' + 'DIV2K_valid_LR_bicubic' + '/' + sc + '/' + corr_name
            for scale in Uscale:
                s = ''
                sc = ''
                if(scale == 'LRunkx2'):
                    s = 'x2'
                    sc = 'X2'
                elif(scale == 'LRunkx3'):
                    s = 'x3'
                    sc = 'X3'
                else:
                    s = 'x4'
                    sc = 'X4'
                corr_name = image_name[:4] + s + image_name[4:]
                image_scales[scale] = main_dir + '/' + 'DIV2K_valid_LR_unknown' + '/' + sc + '/' + corr_name        
            images[image_name] = image_scales
        return images


    def generator(self, images, sample):
        from random import sample
        from IPython.display import Image, display
        import random

        #parameters
        size = 500
        scale = ['LRbicx2', 'LRbicx3', 'LRbicx4']

        #Randomly pick an image name
        names = sample(images.keys().size)
        #build a list of scale image filepaths
        sample = []
        imgs = []
        for name in names:
            sample.append(images[name][random.choice(scale)])

        for image_path in sample:
            imgs.append(image_path)
            print(image_path)
            display(Image(image_path))

        return imgs

    #jared can add this scaling part here how ever he would like
