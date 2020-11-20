import cv2
import matplotlib.pyplot as plt
import random
import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa

# For the children functions, the image path or an image variable will suffice
class DataAugmentor:
    # turns will be the number of clockwise 90 degree rotations
    def perform_rotate(self, imgpath, turns = 1):
        if isinstance(imgpath, str):
            img = cv2.imread(imgpath)
        else:
            img = imgpath
        for i in range (0, turns):
            img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        return img
    
    # By default will flip over the x-axis
    def perform_flip(self, imgpath, horizontally = False):
        if isinstance(imgpath, str):
            img = cv2.imread(imgpath)
        else:
            img = imgpath
        if (horizontally):
            img = cv2.flip(img, 1)
        else:
            img = cv2.flip(img, 0)
        return img
    
    # This will randomly crop a given image with certain width and height constraints. Negative maxvalues mean use whole image
    def perform_crop(self, imgpath, minwidth = 1, minheight = 1, maxwidth = -1, maxheight = -1):
        if isinstance(imgpath, str):
            img = cv2.imread(imgpath)
        else:
            img = imgpath
        height, width, channels = img.shape
        if height < maxheight or maxheight < 1:
            maxheight = height
        if width < maxwidth or maxwidth < 1:
            maxwidth = width
        if minwidth < 1:
            minwidth = 1
        if minheight < 1:
            minheight = 1
        w = round(random.uniform(minwidth, maxwidth))
        x = round(random.uniform(0,width-w))
        h = round(random.uniform(minheight, maxheight))
        y = round(random.uniform(0, height-h))
        crop_img = img[y:y+h, x:x+w]
        return crop_img
    def perform_rotate_custom(self, imgpath, angle):
        if isinstance(imgpath, str):
            img = cv2.imread(imgpath)
        else:
            img = imgpath
        image_center = tuple(np.array(img.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
        result = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)
        return result
    def light_aug_batch(self, imgpath, n):
        if isinstance(imgpath, str):
            img = cv2.imread(imgpath)
        else:
            img = imgpath
            
        images = np.array(
            [img for _ in range(n)],
            dtype=np.uint8
        )
        seq = iaa.Sequential([
        iaa.Fliplr(0.5), # horizontal flips
        iaa.Crop(percent=(0, 0.1)), # random crops
        # Small gaussian blur with random sigma between 0 and 0.5.
        # But we only blur about 50% of all images.
        iaa.Sometimes(
            0.5,
            iaa.GaussianBlur(sigma=(0, 0.5))
        ),
        # Strengthen or weaken the contrast in each image.
        iaa.LinearContrast((0.75, 1.5)),
        # Add gaussian noise.
        # For 50% of all images, we sample the noise once per pixel.
        # For the other 50% of all images, we sample the noise per pixel AND
        # channel. This can change the color (not only brightness) of the
        # pixels.
        iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),
        # Make some images brighter and some darker.
        # In 20% of all cases, we sample the multiplier once per channel,
        # which can end up changing the color of the images.
        iaa.Multiply((0.8, 1.2), per_channel=0.2),
        # Apply affine transformations to each image.
        # Scale/zoom them, translate/move them, rotate them and shear them.
        iaa.Affine(
            scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},
            translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
            rotate=(-25, 25),
            shear=(-8, 8)
        )
        ], random_order=True) # apply augmenters in random order
        return seq(images=images)
    def heavy_aug_batch(self, imgpath, n):
        if isinstance(imgpath, str):
            img = cv2.imread(imgpath)
        else:
            img = imgpath
            
        images = np.array(
            [img for _ in range(n)],
            dtype=np.uint8
        )
        
        sometimes = lambda aug: iaa.Sometimes(0.3, aug)
        seq = iaa.Sequential([
            #
            # Apply the following augmenters to most images.
            #
            iaa.Fliplr(0.5), # horizontally flip 50% of all images
            iaa.Flipud(0.2), # vertically flip 20% of all images

            # crop some of the images by 0-10% of their height/width
            sometimes(iaa.Crop(percent=(0, 0.1))),

            # Apply affine transformations to some of the images
            # - scale to 80-120% of image height/width (each axis independently)
            # - translate by -20 to +20 relative to height/width (per axis)
            # - rotate by -45 to +45 degrees
            # - shear by -16 to +16 degrees
            # - order: use nearest neighbour or bilinear interpolation (fast)
            # - mode: use any available mode to fill newly created pixels
            #         see API or scikit-image for which modes are available
            # - cval: if the mode is constant, then use a random brightness
            #         for the newly created pixels (e.g. sometimes black,
            #         sometimes white)
            sometimes(iaa.Affine(
                scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},
                translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
                rotate=(-45, 45),
                shear=(-16, 16),
                order=[0, 1],
                cval=(0, 255),
                mode=ia.ALL
            )),

            #
            # Execute 0 to 5 of the following (less important) augmenters per
            # image. Don't execute all of them, as that would often be way too
            # strong.
            #
            iaa.SomeOf((0, 5),
                [
                    # Convert some images into their superpixel representation,
                    # sample between 20 and 200 superpixels per image, but do
                    # not replace all superpixels with their average, only
                    # some of them (p_replace).
                    sometimes(
                        iaa.Superpixels(
                            p_replace=(0, 1.0),
                            n_segments=(20, 200)
                        )
                    ),

                    # Blur each image with varying strength using
                    # gaussian blur (sigma between 0 and 3.0),
                    # average/uniform blur (kernel size between 2x2 and 7x7)
                    # median blur (kernel size between 3x3 and 11x11).
                    iaa.OneOf([
                        iaa.GaussianBlur((0, 3.0)),
                        iaa.AverageBlur(k=(2, 7)),
                        iaa.MedianBlur(k=(3, 11)),
                    ]),

                    # Sharpen each image, overlay the result with the original
                    # image using an alpha between 0 (no sharpening) and 1
                    # (full sharpening effect).
                    iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5)),

                    # Same as sharpen, but for an embossing effect.
                    iaa.Emboss(alpha=(0, 1.0), strength=(0, 2.0)),

                    # Search in some images either for all edges or for
                    # directed edges. These edges are then marked in a black
                    # and white image and overlayed with the original image
                    # using an alpha of 0 to 0.7.
                    sometimes(iaa.OneOf([
                        iaa.EdgeDetect(alpha=(0, 0.7)),
                        iaa.DirectedEdgeDetect(
                            alpha=(0, 0.7), direction=(0.0, 1.0)
                        ),
                    ])),
    
                    # Add gaussian noise to some images.
                    # In 50% of these cases, the noise is randomly sampled per
                    # channel and pixel.
                    # In the other 50% of all cases it is sampled once per
                    # pixel (i.e. brightness change).
                    iaa.AdditiveGaussianNoise(
                        loc=0, scale=(0.0, 0.05*255), per_channel=0.5
                    ),

                    # Either drop randomly 1 to 10% of all pixels (i.e. set
                    # them to black) or drop them on an image with 2-5% percent
                    # of the original size, leading to large dropped
                    # rectangles.
                    iaa.OneOf([
                        iaa.Dropout((0.01, 0.1), per_channel=0.5),
                        iaa.CoarseDropout(
                            (0.03, 0.15), size_percent=(0.02, 0.05),
                            per_channel=0.2
                        ),
                    ]),

                    # Invert each image's channel with 5% probability.
                    # This sets each pixel value v to 255-v.
                    iaa.Invert(0.05, per_channel=True), # invert color channels

                    # Add a value of -10 to 10 to each pixel.
                    iaa.Add((-10, 10), per_channel=0.5),

                    # Change brightness of images (50-150% of original value).
                    iaa.Multiply((0.5, 1.5), per_channel=0.5),

                    # Improve or worsen the contrast of images.
                    iaa.LinearContrast((0.5, 2.0), per_channel=0.5),

                    # Convert each image to grayscale and then overlay the
                    # result with the original with random alpha. I.e. remove
                    # colors with varying strengths.
                    iaa.Grayscale(alpha=(0.0, 1.0)),

                    # In some images move pixels locally around (with random
                    # strengths).
                    sometimes(
                        iaa.ElasticTransformation(alpha=(0.5, 3.5), sigma=0.25)
                    ),

                    # In some images distort local areas with varying strength.
                    sometimes(iaa.PiecewiseAffine(scale=(0.01, 0.05)))
                ],
                # do all of the above augmentations in random order
                random_order=True
            )
        ],
        # do all of the above augmentations in random order
        random_order=True
        )
        return seq(images=images)
#Example on how to use this code:
#import matplotlib.pyplot as plt
# (import this code)
#datagen = DataAugmentor()
#resimg = datagen.perform_rotate("C:\\Users\\Jared Habermehl\\Documents\\2020-Image-Super-Resolution\\big_im_SR.png")
#resimg = datagen.perform_flip(resimg)
#plt.axis("off")
#plt.imshow(cv2.cvtColor(resimg, cv2.COLOR_BGR2RGB))
#plt.show()