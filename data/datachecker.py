import os.path
from os import path
import glob
from PIL import Image  

# Verify that Set5 is present and complete. 
#print("\nDATASET: Set5")
errors = []
if path.exists('Set5'):
    valid_subsets = ['x2', 'x3', 'x4', 'x8']
    # Verify that dataset has all of the required subsets.
    for s in valid_subsets:
        subset = 'Set5/' + s
        if path.exists(subset):
            # Verify that each subset has the correct number of images. 
            invalid_images = len(glob.glob1(subset,"*.png")) - 5
            if(invalid_images < 0):
                errors.append(subset + " has " + str(-1 * invalid_images) + " missing images")
            elif (invalid_images > 0):
                errors.append(subset + " has " + str(invalid_images) + " extra images")
        else:
            print(subset + " is a missing subset")
    # Check if dataset contains extra directories. 
    for s in [subset for subset in os.listdir('Set5') if subset not in valid_subsets]:
        errors.append('Set5/' + s + " is an extra directory.")
else:
    errors.append("Set5 is a missing dataset")
if errors == []:
    errors.append("Set5 is a complete dataset.")
    Image.open('Set5/x2/baby_LRBI_x2.png').show()
else:
    for error in errors:
        print(error)

# Verify that Set14 is present and complete.
#print("\nDATASET: Set14")
if path.exists('Set14'):
    print("Placeholder")
else:
    print("Set14 is a missing dataset")