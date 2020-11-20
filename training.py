import tensorflow as tf
import sys
from data import DataGenerator
from model import espcn, psnr

# Trains model and saves weights
def train(model, r, batch_size, epochs): 
    # Fit model
    training_generator = DataGenerator('LRbicx' + str(r), batch_size = batch_size)
    model.fit_generator(generator = training_generator, epochs=epochs, verbose=1)
    # Save weights
    # Filepath where the weights will be saved to
    filepath = 'model/weights/r' + str(r) + 'bs' + str(batch_size) + 'epochs' + str(epochs) +  'weights.h5'
    model.save_weights(filepath)
    print("Saved weights at : " + filepath)

if __name__ == "__main__":    
    if len(sys.argv) == 4:
        # Parameters
        r = int(sys.argv[1])
        batch_size = int(sys.argv[2])
        epochs = int(sys.argv[3])
        # Compile model
        opt = tf.keras.optimizers.Adam(learning_rate=0.001)
        # Peak Signal-to-Noise Ratio
        def PSNR(y_true, y_pred):
            max_pixel = 1.0
            return tf.image.psnr(y_true, y_pred, max_val=max_pixel)
        model = espcn(r)
        model.compile(optimizer=opt, loss='mse', metrics=[PSNR])
        train(model, r, batch_size, epochs)
    else:
        print("Correct usage: python training.py [upscale_factor] [batch_size] [epochs]")