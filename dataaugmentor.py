import cv2
import random

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

#Example on how to use this code:
#import matplotlib.pyplot as plt
# (import this code)
#datagen = DataAugmentor()
#resimg = datagen.perform_rotate("C:\\Users\\Jared Habermehl\\Documents\\2020-Image-Super-Resolution\\big_im_SR.png")
#resimg = datagen.perform_flip(resimg)
#plt.axis("off")
#plt.imshow(cv2.cvtColor(resimg, cv2.COLOR_BGR2RGB))
#plt.show()
 