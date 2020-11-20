import sys
import tensorflow as tf
from data import DataGenerator
from model import espcn, psnr

# Calculates PSNRs and cumulative average PSNR of the testing dataset
def benchmark(weights_filename, r, verbose = "True"):
    filepath = 'model/weights/' + weights_filename # filepath of weights
    num_images = 729 # number of testing images to benchmark on (<=729)
    if verbose == "True":
        verbose = True
    else:
        verbose = False
    
    # Compile model
    opt = tf.keras.optimizers.Adam(learning_rate=0.001)
    # Peak Signal-to-Noise Ratio
    def PSNR(y_true, y_pred):
        max_pixel = 1.0
        return tf.image.psnr(y_true, y_pred, max_val=max_pixel)
    model = espcn(r)
    model.compile(optimizer=opt, loss='mse', metrics=[PSNR])
    # Initialize testing generator
    testing_generator = DataGenerator('LRbicx' + str(r), batch_size = 1, dictionary = "test")
    # Load weights
    model.load_weights(filepath)
    # Calculate average PSNR of all testing data
    average_psnr = 0
    for i in range(0, num_images):
        lr, hr = testing_generator.__getitem__(i)
        sr = model.predict(lr)
        result = psnr(sr[0], hr[0])
        average_psnr += result
        if verbose:
            print('Image: ' + str(i) + ', PSNR: ' + str(result) + ', Average: ' + str(average_psnr/(i+1)))
    print("Average PSNR: " + str(average_psnr/num_images))

if __name__ == "__main__":    
    # Parameters
    weights_filename = sys.argv[1]
    upscale_factor = int(sys.argv[2])
    if len(sys.argv) == 3:
        benchmark(weights_filename, upscale_factor)
    if len(sys.argv) == 4:
        verbose = sys.argv[3]
        benchmark(weights_filename, upscale_factor, verbose)
    else:
        print ('Correct usage: python benchmark.py [weights_filename] [upscale_factor] [off (optional)]')